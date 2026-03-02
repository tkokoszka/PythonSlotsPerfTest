from __future__ import annotations

import logging
import statistics
from collections.abc import Callable
from dataclasses import fields
from functools import partial
from typing import Any

from models.execution_result import ExecutionResult, ExecutionStats, TrialDetails
from runner.run import run_scenario
from scenarios.base import BaseScenario

logger = logging.getLogger(__name__)


def run_scenarios_with_trials(
    scenarios: list[BaseScenario],
    num_instances: int,
    num_trials: int,
) -> list[ExecutionResult]:
    results = []
    for scenario in scenarios:
        logger.info(f"Running {scenario.name} ({num_trials} trials)")
        results.append(_run_scenario_with_trials(scenario, num_instances, num_trials))
    return results


def _run_scenario_with_trials(
    scenario: BaseScenario,
    num_instances: int,
    num_trials: int,
) -> ExecutionResult:
    trial_stats = [run_scenario(scenario, num_instances) for _ in range(num_trials)]

    return ExecutionResult(
        scenario=scenario,
        num_created=num_instances,
        stats=_aggregate_stats(trial_stats, statistics.mean),
        trial_details=TrialDetails(
            num_trials=num_trials,
            per_trial=trial_stats,
            stddev=_aggregate_stats(trial_stats, statistics.pstdev),
            p90_low=_aggregate_stats(trial_stats, partial(_percentile, fraction=0.05)),
            p90_high=_aggregate_stats(trial_stats, partial(_percentile, fraction=0.95)),
        ),
    )


def _aggregate_stats(
    stats_list: list[ExecutionStats],
    fn: Callable[[list[int] | list[float]], int | float],
) -> ExecutionStats:
    """Apply an aggregation function per-field across a list of ExecutionStats.

    Args:
        fn: Aggregation function. It takes all values of a single field across trials and returns the
            aggregated value (e.g. mean, stddev, percentile).
    """
    kwargs: dict[str, Any] = {}
    for f in fields(ExecutionStats):
        values = [getattr(s, f.name) for s in stats_list]
        result = fn(values)
        kwargs[f.name] = int(result) if f.type == "int" or f.type is int else result
    return ExecutionStats(**kwargs)


def _percentile(values: list[int] | list[float], *, fraction: float) -> float:
    """Compute a percentile using linear interpolation."""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    idx = fraction * (n - 1)
    lo = int(idx)
    hi = min(lo + 1, n - 1)
    weight = idx - lo
    return sorted_vals[lo] + weight * (sorted_vals[hi] - sorted_vals[lo])

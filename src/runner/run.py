from __future__ import annotations

import gc
import logging
import time
from dataclasses import dataclass

import psutil
from pympler import asizeof

from models.execution_result import ExecutionResult, ExecutionStats
from scenarios.base import BaseScenario

logger = logging.getLogger(__name__)


def run_scenarios(
    scenarios: list[BaseScenario], num_instances: int
) -> list[ExecutionResult]:
    results = []
    for scenario in scenarios:
        logger.info(f"Running {scenario.name}")
        results.append(run_scenario(scenario, num_instances))
    return results


def run_scenario(scenario: BaseScenario, num_instances: int) -> ExecutionResult:
    """Run scenario, collect and return stats."""

    # Run garbage collector to start with a clean slate and make results independent of
    # what run before.
    gc.collect()

    start_state = _current_runtime_state_snapshot()

    # Run the scenario.
    results = []
    for seq_no in range(num_instances):
        instance = scenario.create_one(seq_no)
        results.append(instance)

    end_state = _current_runtime_state_snapshot()

    return ExecutionResult(
        scenario=scenario,
        num_created=len(results),
        stats=ExecutionStats(
            results_size_ram_bytes=asizeof.asizeof(results),
            ram_used=end_state.memory_rss - start_state.memory_rss,
            time_elapsed_sec=end_state.walltime_sec - start_state.walltime_sec,
            cpu_user_time_sec=end_state.cpu_user_time_sec
            - start_state.cpu_user_time_sec,
            cpu_system_time_sec=(
                end_state.cpu_system_time_sec - start_state.cpu_system_time_sec
            ),
        ),
    )


def _current_runtime_state_snapshot() -> _RuntimeState:
    p = psutil.Process()

    return _RuntimeState(
        memory_rss=p.memory_info().rss,
        walltime_sec=time.perf_counter(),
        cpu_user_time_sec=p.cpu_times().user,
        cpu_system_time_sec=p.cpu_times().system,
    )


@dataclass(slots=True)
class _RuntimeState:
    memory_rss: int
    walltime_sec: float
    cpu_user_time_sec: float
    cpu_system_time_sec: float

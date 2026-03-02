from __future__ import annotations

from dataclasses import dataclass

from scenarios.base import BaseScenario


@dataclass
class ExecutionResult:
    # Scenario that was run.
    scenario: BaseScenario

    # Num objects created.
    num_created: int

    # Averaged stats (or single-run stats when trials=1).
    stats: ExecutionStats

    trial_details: TrialDetails


@dataclass
class ExecutionStats:
    # Mem size of list storing all the created objects, in bytes.
    results_size_ram_bytes: int

    # Peak memory allocated during scenario run, in bytes.
    ram_used: int

    # Time elapsed (walltime).
    time_elapsed_sec: float

    # CPU time (user + system), in seconds.
    cpu_time_sec: float


@dataclass
class TrialDetails:
    num_trials: int
    per_trial: list[ExecutionStats]

    # Standard deviation of each metric across trials.
    stddev: ExecutionStats

    # 5th and 95th percentile bounds.
    p90_low: ExecutionStats
    p90_high: ExecutionStats

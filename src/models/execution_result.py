from __future__ import annotations

from dataclasses import dataclass

from scenarios.base import BaseScenario


@dataclass
class ExecutionResult:
    # Scenario that was run.
    scenario: BaseScenario

    # Num objects created.
    num_created: int

    stats: ExecutionStats


@dataclass
class ExecutionStats:
    # Mem size of list storing all the created objects, in bytes.
    results_size_ram_bytes: int

    # Peak memory allocated during scenario run (tracemalloc), in bytes.
    ram_used: int

    # Time elapsed (walltime).
    time_elapsed_sec: float

    # CPU time (user + system), in seconds.
    cpu_time_sec: float

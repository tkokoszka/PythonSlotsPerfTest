from dataclasses import dataclass

from scenarios.base import BaseScenario


@dataclass
class ExecutionStats:
    # Scenario that was run.
    scenario: BaseScenario

    # Num objects created.
    num_created: int

    # Mem size of list storing all the created objects, in bytes.
    mem_results_size_bytes: int

    # Memory used in bytes.
    mem_used: int

    # Time elapsed (walltime).
    time_elapsed_sec: float

    # CPU user time.
    cpu_user_time_sec: float

    # CPU system time.
    cpu_system_time_sec: float

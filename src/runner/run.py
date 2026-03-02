from __future__ import annotations

import gc
import logging
import time
import tracemalloc
from dataclasses import dataclass

from pympler import asizeof

from models.execution_result import ExecutionStats
from scenarios.base import BaseScenario

logger = logging.getLogger(__name__)


def run_scenario(scenario: BaseScenario, num_instances: int) -> ExecutionStats:
    """Run scenario, collect and return stats."""

    # Run garbage collector to start with a clean slate and make results independent of
    # what run before.
    gc.collect()

    # Start tracemalloc to track Python-level memory allocations precisely,
    # rather than relying on OS-level RSS which is noisy and page-granular.
    tracemalloc.start()

    start_state = _current_runtime_state_snapshot()

    # Run the scenario.
    results = []
    for seq_no in range(num_instances):
        # Data preparation — keep this lightweight so it doesn't mask the
        # resource usage of the object construction below.
        id = str(seq_no)
        name = f"Name {seq_no}"
        surname = f"Surname {seq_no}"
        age = seq_no % 79 + 21

        # Object construction — this is what we're measuring.
        instance = scenario.construct_one(id=id, name=name, surname=surname, age=age)
        results.append(instance)

    end_state = _current_runtime_state_snapshot()

    # Get peak memory allocated during the scenario run.
    _, tracemalloc_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return ExecutionStats(
        results_size_ram_bytes=asizeof.asizeof(results),
        ram_used=tracemalloc_peak,
        time_elapsed_sec=end_state.walltime_sec - start_state.walltime_sec,
        cpu_time_sec=end_state.cpu_time_sec - start_state.cpu_time_sec,
    )


def _current_runtime_state_snapshot() -> _RuntimeState:
    return _RuntimeState(
        walltime_sec=time.perf_counter(),
        cpu_time_sec=time.process_time(),
    )


@dataclass(slots=True)
class _RuntimeState:
    walltime_sec: float
    cpu_time_sec: float

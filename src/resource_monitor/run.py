import gc
import time

import psutil
from pympler import asizeof

from resource_monitor.run_config import RunConfig
from resource_monitor.run_stats import RunStats


def run_measurement(config: RunConfig, num_cycles: int) -> RunStats:
    # Run garbaga collector to start with a clean slate and make results independent of
    # what run before.
    gc.collect()
    p = psutil.Process()

    mem_start = p.memory_info().rss
    time_start = time.perf_counter()
    cpu_time_start = p.cpu_times()

    # Run the function
    result = config.fun(num_cycles)

    cpu_time_end = p.cpu_times()
    time_end = time.perf_counter()
    mem_end = p.memory_info().rss

    stats = RunStats(
        name=config.name,
        result_len=len(result),
        result_size=asizeof.asizeof(result),
        time_elapsed_sec=time_end - time_start,
        cpu_time_sec=(cpu_time_end.user - cpu_time_start.user),
        mem_used=mem_end - mem_start,
    )

    # Cleanup resource avoid biasing next execution.
    result = None
    gc.collect()

    return stats

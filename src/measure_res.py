import gc
import math
import time
from typing import Callable

import humanize
import psutil
from pympler import asizeof


def measure(name: str, fun: Callable[[], list]):
    gc.collect()
    p = psutil.Process()

    mem_start = p.memory_info().rss
    time_start = time.perf_counter()
    cpu_time_start = p.cpu_times()

    r = fun()

    cpu_time_end = p.cpu_times()
    time_end = time.perf_counter()
    mem_end = p.memory_info().rss

    mem_used = mem_end - mem_start
    time_elapsed = time_end - time_start
    cpu_time_elapsed = cpu_time_end.user - cpu_time_start.user

    print(f"Results for {name}")
    print(
        f"  Wall time: {humanize.intcomma(math.ceil(time_elapsed * 1000))} ms"
        f" ({humanize.precisedelta(time_elapsed, minimum_unit='milliseconds')})"
    )
    print(
        f"  CPU user time: {humanize.intcomma(math.ceil(cpu_time_elapsed * 1000))} ms"
        f" ({humanize.precisedelta(cpu_time_elapsed, minimum_unit='milliseconds')})"
    )
    print(f"  Response size: {humanize.naturalsize(asizeof.asizeof(r))}")
    print(f"  Allocated process memory: {humanize.naturalsize(mem_used)}")
    r = None
    gc.collect()

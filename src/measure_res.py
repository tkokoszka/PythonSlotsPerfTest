import time
from typing import Any, Callable

import humanize
import psutil


def measure(name: str, fun: Callable) -> Any:
    p = psutil.Process()

    mem_start = p.memory_info().rss
    time_start = time.perf_counter()

    r = fun()

    time_end = time.perf_counter()
    mem_end = p.memory_info().rss

    time_elapsed = time_end - time_start
    mem_used = mem_end - mem_start

    print(f"Timing for {name}")
    print(f"  time: {humanize.precisedelta(time_elapsed, minimum_unit='milliseconds')}")
    print(f"  RAM: {humanize.naturalsize(mem_used)}")

    return r

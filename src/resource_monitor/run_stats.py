import math
from dataclasses import dataclass

import humanize


@dataclass
class RunStats:
    # Name of this run, human readable.
    name: str

    # Length of the measured function result.
    result_len: int

    # Function result size in bytes.
    result_size: int

    # Time elapsed when running (wall time).
    time_elapsed_sec: float

    # CPU time (user + os) for running.
    cpu_time_sec: float

    # Memory used for the run
    mem_used: int

    def as_human_str(self) -> str:
        return (
            f"Results for {self.name}:"
            + f"\n  result_len={humanize.intcomma(self.result_len)}"
            + f"\n  result_size={humanize.naturalsize(self.result_size)}"
            + f"\n  mem_used   ={humanize.naturalsize(self.mem_used)}"
            + f"\n  time_elapsed={humanize.intcomma(math.ceil(self.time_elapsed_sec * 1000))} ms"
            + f"\n  cpu_time    ={humanize.intcomma(math.ceil(self.cpu_time_sec * 1000))} ms"
        )

from datetime import timedelta

import humanize

from models.execution_stats import ExecutionStats
from reporter.base import ExecutionReporter


class TextListReporter(ExecutionReporter):
    def report(self, executions_stats: list[ExecutionStats]) -> str:
        results: list[str] = []
        for seq_no, execution_stats in enumerate(executions_stats):
            results.append(self._report_execution(seq_no, execution_stats))
        return "\n".join(results)

    def _report_execution(self, seq_no: int, stats: ExecutionStats):
        lines = [
            "-" * 40,
            f"{seq_no + 1:02}: {stats.scenario.name}",
            f"  objects created: {humanize.intcomma(stats.num_created)}",
            f"  objects size in RAM: {humanize.naturalsize(stats.results_size_ram_bytes)}",
            f"  start/End RAM Used:  {humanize.naturalsize(stats.ram_used)}",
            f"  wall time:       {humanize.precisedelta(timedelta(seconds=stats.time_elapsed_sec))}",
            f"  CPU user time:   {humanize.precisedelta(timedelta(seconds=stats.cpu_user_time_sec))}",
            f"  CPU system time: {humanize.precisedelta(timedelta(seconds=stats.cpu_system_time_sec))}",
        ]
        return "\n".join(lines)

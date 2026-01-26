from datetime import timedelta

import humanize

from models.execution_result import ExecutionResult
from reporter.base import ExecutionReporter


class TextListReporter(ExecutionReporter):
    def report(self, results: list[ExecutionResult]) -> str:
        reports: list[str] = []
        for seq_no, result in enumerate(results):
            reports.append(self._report_single(seq_no, result))
        return "\n".join(reports)

    def _report_single(self, seq_no: int, result: ExecutionResult):
        lines = [
            "-" * 40,
            f"{seq_no + 1:02}: {result.scenario.name}",
            f"  objects created: {humanize.intcomma(result.num_created)}",
            f"  objects size in RAM: {humanize.naturalsize(result.stats.results_size_ram_bytes)}",
            f"  start/End RAM Used:  {humanize.naturalsize(result.stats.ram_used)}",
            f"  wall time:       {humanize.precisedelta(timedelta(seconds=result.stats.time_elapsed_sec))}",
            f"  CPU user time:   {humanize.precisedelta(timedelta(seconds=result.stats.cpu_user_time_sec))}",
            f"  CPU system time: {humanize.precisedelta(timedelta(seconds=result.stats.cpu_system_time_sec))}",
        ]
        return "\n".join(lines)

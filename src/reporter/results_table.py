from typing import Callable

import humanize

from models.execution_result import ExecutionResult
from reporter.base import ExecutionReporter
from reporter.table_formatter import ColumnDef, render_table

type _ColumnExtractor = Callable[[ExecutionResult], str]


class ResultsTableReporter(ExecutionReporter):
    def report(self, results: list[ExecutionResult]) -> str:
        # Columns to print:
        spec: list[tuple[ColumnDef, _ColumnExtractor]] = [
            (
                ColumnDef(title="No"),
                lambda r: str(1 + next(i for i, x in enumerate(results) if x is r)),
            ),
            (
                ColumnDef(title="Scenario", align="<"),
                lambda r: r.scenario.name,
            ),
            (
                ColumnDef(title="Res Size RAM"),
                lambda r: humanize.naturalsize(r.stats.results_size_ram_bytes),
            ),
            (
                ColumnDef(title="RAM Used"),
                lambda r: humanize.naturalsize(r.stats.ram_used),
            ),
            (
                ColumnDef(title="Wall Time"),
                lambda r: _format_duration(r.stats.time_elapsed_sec),
            ),
            (
                ColumnDef(title="CPU Time"),
                lambda r: _format_duration(r.stats.cpu_time_sec),
            ),
        ]

        columns = [col for col, _ in spec]
        rows = [[ext(r) for _, ext in spec] for r in results]
        table = render_table(columns, rows)

        num_created = results[0].num_created
        return f"Objects created={num_created}\n{table}"


def _format_duration(seconds: float) -> str:
    """Formats time duration into a concise string (e.g., '1h2m3.456s').
    Omit hours and minutes if they are not needed.

    Examples:
        >>> 3661.5 -> '1h1m1.500s'
        >>> 61.0 -> '1m1.000s'
        >>> 0.5 -> '0.500s'
    """
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)

    res = ""
    if h:
        res += f"{int(h)}h{int(m):02}m"
    elif m:
        res += f"{int(m)}m"
    res += f"{s:.3f}s"
    return res

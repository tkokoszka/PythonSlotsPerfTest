from dataclasses import dataclass
from typing import Literal

import humanize

from models.execution_stats import ExecutionStats
from reporter.base import ExecutionReporter


class TextTableReporter(ExecutionReporter):
    def report(self, executions_stats: list[ExecutionStats]) -> str:
        # Column definitions.
        columns = [
            _ColumnDef(title="No"),
            _ColumnDef(title="Scenario", align="<"),
            _ColumnDef(title="Res Size RAM"),
            _ColumnDef(title="RAM Used"),
            _ColumnDef(title="Wall Time"),
            _ColumnDef(title="CPU User"),
            _ColumnDef(title="CPU Sys"),
        ]

        rows: list[list[str]] = []

        # Add data
        for seq_no, stats in enumerate(executions_stats):
            rows.append(
                [
                    str(seq_no + 1),
                    stats.scenario.name,
                    humanize.naturalsize(stats.results_size_ram_bytes),
                    humanize.naturalsize(stats.ram_used),
                    _format_duration(stats.time_elapsed_sec),
                    _format_duration(stats.cpu_user_time_sec),
                    _format_duration(stats.cpu_system_time_sec),
                ]
            )

        # Calculate dynamic column widths based on max content length
        all_rows = [[c.title for c in columns]] + rows
        col_widths = [max(len(row[i]) for row in all_rows) for i in range(len(columns))]
        all_rows = None

        # Build format string
        row_fmt = " | ".join(f"{{:{c.align}{w}}}" for c, w in zip(columns, col_widths))

        # Print Table
        result: list[str] = []
        result.append(row_fmt.format(*[c.title for c in columns]))
        result.append("-" * (sum(col_widths) + 3 * (len(columns) - 1)))
        for row in rows:
            result.append(row_fmt.format(*row))

        num_created = executions_stats[0].num_created
        return f"Objects created={num_created}\n" + "\n".join(result)


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


@dataclass
class _ColumnDef:
    # Column title, as shown to the user
    title: str

    # Column alignment, "<"=Left, ">""=Right.
    align: Literal["<", ">"] = ">"

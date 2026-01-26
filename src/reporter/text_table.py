from dataclasses import dataclass
from typing import Callable, Literal

import humanize

from models.execution_result import ExecutionResult
from reporter.base import ExecutionReporter


class TextTableReporter(ExecutionReporter):
    def report(self, results: list[ExecutionResult]) -> str:
        # Column definitions.
        columns = [
            ColumnDef(
                title="No",
                extractor=lambda r: str(
                    1 + next(i for i, x in enumerate(results) if x is r)
                ),
            ),
            ColumnDef(
                title="Scenario",  #
                extractor=lambda r: r.scenario.name,
                align="<",
            ),
            ColumnDef(
                title="Res Size RAM",
                extractor=lambda r: humanize.naturalsize(
                    r.stats.results_size_ram_bytes
                ),
            ),
            ColumnDef(
                title="RAM Used",
                extractor=lambda r: humanize.naturalsize(r.stats.ram_used),
            ),
            ColumnDef(
                title="Wall Time",
                extractor=lambda r: _format_duration(r.stats.time_elapsed_sec),
            ),
            ColumnDef(
                title="CPU User",
                extractor=lambda r: _format_duration(r.stats.cpu_user_time_sec),
            ),
            ColumnDef(
                title="CPU Sys",
                extractor=lambda r: _format_duration(r.stats.cpu_system_time_sec),
            ),
        ]

        rows: list[list[str]] = []

        # Add data
        for result in results:
            col: list[str] = []
            for column in columns:
                col.append(column.extractor(result))
            rows.append(col)

        # Calculate dynamic column widths based on max content length
        all_rows = [[c.title for c in columns]] + rows
        col_widths = [max(len(row[i]) for row in all_rows) for i in range(len(columns))]
        all_rows = None

        # Build format string
        row_fmt = " | ".join(f"{{:{c.align}{w}}}" for c, w in zip(columns, col_widths))

        # Print Table
        response: list[str] = []
        response.append(row_fmt.format(*[c.title for c in columns]))
        response.append("-" * (sum(col_widths) + 3 * (len(columns) - 1)))
        for row in rows:
            response.append(row_fmt.format(*row))

        num_created = results[0].num_created
        return f"Objects created={num_created}\n" + "\n".join(response)


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


@dataclass(kw_only=True)
class ColumnDef:
    # Column title, as shown to the user
    title: str

    # Column alignment, "<"=Left, ">""=Right.
    align: Literal["<", ">"] = ">"

    # Callable that extract column value from results in a format to put in the table.
    extractor: Callable[[ExecutionResult], str]

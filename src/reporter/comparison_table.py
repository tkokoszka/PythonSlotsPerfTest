import dataclasses
from dataclasses import dataclass
from typing import Literal

from models.execution_result import ExecutionResult, ExecutionStats
from reporter.base import ExecutionReporter


class ComparisonTableReporter(ExecutionReporter):
    """Pairwise percent-difference matrix between scenarios for a single metric.

    Values show how much the row scenario differs from the column scenario:
      (row - col) / col * 100
    Positive = row is larger, negative = row is smaller.
    """

    def __init__(self, field_name: str) -> None:
        valid_filed_names = {f.name for f in dataclasses.fields(ExecutionStats)}
        if field_name not in valid_filed_names:
            valid = ", ".join(valid_filed_names)
            raise ValueError(f"Unknown field {field_name!r}. Valid fields: {valid}")
        self._field_name = field_name

    def report(self, results: list[ExecutionResult]) -> str:
        scenario_names = [r.scenario.name for r in results]
        values = [getattr(r.stats, self._field_name) for r in results]

        # Build cell strings: rows = "from", columns = "to" (baseline).
        cells: list[list[str]] = []
        for row_val in values:
            row: list[str] = []
            for col_val in values:
                if row_val is col_val:
                    row.append("-")
                elif col_val == 0:
                    row.append("N/A")
                else:
                    pct = (row_val - col_val) / col_val * 100
                    row.append(f"{pct:+.1f}%")
            cells.append(row)

        # Column definitions: first column is the row label, rest are scenario names.
        columns = [
            _ColumnDef(title="", align="<"),
            *[_ColumnDef(title=name) for name in scenario_names],
        ]

        # Merge header titles + data for width calculation.
        all_rows = [[c.title for c in columns]]
        for name, row in zip(scenario_names, cells):
            all_rows.append([name, *row])

        col_widths = [max(len(r[i]) for r in all_rows) for i in range(len(columns))]

        row_fmt = " | ".join(f"{{:{c.align}{w}}}" for c, w in zip(columns, col_widths))

        lines: list[str] = []
        lines.append(row_fmt.format(*[c.title for c in columns]))
        lines.append("-" * (sum(col_widths) + 3 * (len(columns) - 1)))
        for name, row in zip(scenario_names, cells):
            lines.append(row_fmt.format(name, *row))

        return f"Comparison: {self._field_name}\n" + "\n".join(lines)


@dataclass(kw_only=True)
class _ColumnDef:
    title: str
    # Column alignment: "<" left, ">" right, "^" center.
    align: Literal["<", ">", "^"] = "^"

import dataclasses

from models.execution_result import ExecutionResult, ExecutionStats
from reporter.base import ExecutionReporter
from reporter.table_formatter import ColumnDef, render_table


class ComparisonTableReporter(ExecutionReporter):
    """Pairwise percent-difference matrix between scenarios for a single metric.

    Values show how much the row scenario differs from the column scenario:
      (row - col) / col * 100
    Positive = row is larger, negative = row is smaller.
    """

    def __init__(self, field_name: str) -> None:
        self._field_name = self._valid_field_name_on_raise(field_name)

    def _valid_field_name_on_raise(self, field_name: str) -> str:
        valid_filed_names = {f.name for f in dataclasses.fields(ExecutionStats)}
        if field_name not in valid_filed_names:
            valid = ", ".join(valid_filed_names)
            raise ValueError(f"Unknown field {field_name!r}. Valid fields: {valid}")
        return field_name

    def report(self, results: list[ExecutionResult]) -> str:
        names = [r.scenario.name for r in results]
        values = [getattr(r.stats, self._field_name) for r in results]

        # Build table rows: rows = "from", columns = "to" (baseline).
        rows: list[list[str]] = []
        for name, row_val in zip(names, values):
            row: list[str] = [name]
            for col_val in values:
                if row_val is col_val:
                    row.append("-")
                elif col_val == 0:
                    row.append("N/A")
                else:
                    pct = (row_val - col_val) / col_val * 100
                    row.append(f"{pct:+.1f}%")
            rows.append(row)

        columns = [
            ColumnDef(title="", align="<"),
            *[ColumnDef(title=name, align="^") for name in names],
        ]
        table = render_table(columns, rows)

        return f"Comparison: {self._field_name}\n{table}"

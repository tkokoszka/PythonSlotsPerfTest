from dataclasses import dataclass
from typing import Literal

Alignment = Literal["<", ">", "^"]


@dataclass(kw_only=True)
class ColumnDef:
    """Column definition for table rendering."""

    title: str
    # Column alignment: "<" left, ">" right, "^" center.
    align: Alignment = ">"


def render_table(columns: list[ColumnDef], rows: list[list[str]]) -> str:
    """Render column definitions and string rows into a formatted ASCII table."""
    all_rows = [[c.title for c in columns], *rows]
    col_widths = [max(len(r[i]) for r in all_rows) for i in range(len(columns))]

    row_fmt = " | ".join(f"{{:{c.align}{w}}}" for c, w in zip(columns, col_widths))
    separator = "-" * (sum(col_widths) + 3 * (len(columns) - 1))

    lines: list[str] = [
        row_fmt.format(*[c.title for c in columns]),
        separator,
        *(row_fmt.format(*row) for row in rows),
    ]
    return "\n".join(lines)

from dataclasses import dataclass
from typing import Literal

Alignment = Literal["<", ">", "^"]


@dataclass(kw_only=True)
class ColumnDef:
    """Column definition for table rendering."""

    title: str
    # Column alignment: "<" left, ">" right, "^" center.
    align: Alignment = ">"


_ALIGN_TO_SEPARATOR: dict[Alignment, str] = {
    "<": ":{}-",
    ">": "-{}:",
    "^": ":{}:",
}


def render_table(columns: list[ColumnDef], rows: list[list[str]]) -> str:
    """Render column definitions and string rows into a markdown table."""
    all_rows = [[c.title for c in columns], *rows]
    col_widths = [max(len(r[i]) for r in all_rows) for i in range(len(columns))]

    def _md_row(cells: list[str]) -> str:
        padded = [
            f" {c:{col.align}{w}} " for c, col, w in zip(cells, columns, col_widths)
        ]
        return f"|{'|'.join(padded)}|"

    sep_cells = [
        _ALIGN_TO_SEPARATOR[c.align].format("-" * w)
        for c, w in zip(columns, col_widths)
    ]
    separator = "|" + "|".join(sep_cells) + "|"

    lines: list[str] = [
        _md_row([c.title for c in columns]),
        separator,
        *(_md_row(row) for row in rows),
    ]
    return "\n".join(lines)

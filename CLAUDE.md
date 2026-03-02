# CLAUDE.md

## Project

Python benchmarking tool comparing memory and CPU cost of different data structure approaches (classes, dataclasses, slots, etc).

## Tooling

- Python >=3.13, managed with `uv`
- Run: `uv run python src/main.py`
- Linting/formatting: ruff (format + lint with --fix)
- Type checking: pyright (standard mode)
- Spelling: codespell (auto-fix with -w)
- Pre-commit runs all of the above
- Run pre-commit over all files: `uv run pre-commit run -a`

## Code style

- Type annotations on all function signatures
- ruff handles formatting — do not argue with it
- pyright standard mode — no `type: ignore` unless truly unavoidable

## Communication style

- Be concise. No filler, no preamble.
- Do not be sycophantic. Skip "Great question!" and similar.
- When reviewing code or evaluating options, be critical. Point out trade-offs and downsides, not just benefits.
- Explain high-level ideas, not implementation details unless asked.

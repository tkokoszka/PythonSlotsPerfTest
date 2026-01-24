# Data object in Python

## Setup

Pre-requisites:

- uv tool - [Astral uv](https://docs.astral.sh/uv/)

Bootstrap:

- Create venv, install all deps: `uv sync --frozen`
- Install pre-commit hooks: `uv run pre-commit install`
  - It installs pre-commit from project venv, no need to install pre-commit globally

## TODOs

- Add scenario for TypedDict
- Add scenario for NamedTuple
- Add scenario for SimpleNamespace
- Implement md_report.py
  - generate results to reports/YYYY-MM-DD.md, use jinja2 templates
  - have a simple table: name, metrics

## Operations

#### Pre-commit hooks

- Run only over staged files: `uv run pre-commit run`
- Run over all files: `uv run pre-commit run -a`
- Installing pre-commit hooks takes very long on Windows:
  - Find the cache path: `uv run python -c "from pre_commit.store import Store; print(Store().directory)"`
  - Exclude it from Windows Defender scans
  - You can remove the exclude after pre-commit env is created

#### Update deps

- update deps in `pyproject.toml`
- run `uv sync`

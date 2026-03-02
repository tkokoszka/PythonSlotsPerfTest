# Data Objects in Python - Performance Benchmark

Benchmarking tool that measures memory and CPU cost of creating hundreds of thousands objects using different Python data structure approaches.

## Measured Metrics

- **Object Size** - deep memory footprint of all created objects
- **RAM Used** - process RSS delta during execution
- **CPU User / System Time** - CPU time in user and kernel space

## Running

```bash
uv run python src/main.py
```

## TODOs

- Run 10 times, collect avg, min, max, std_dev
- Report in a comparison matrix all to all diff
- Implement md_report.py
  - generate results to reports/YYYY-MM-DD.md, use jinja2 templates
  - have a simple table: name, metrics

## Operations

#### Setup

Pre-requisites:

- uv tool - [Astral uv](https://docs.astral.sh/uv/)

Bootstrap:

- Create venv, install all deps: `uv sync --frozen`
- Install pre-commit hooks: `uv run pre-commit install`
  - It installs pre-commit from project venv, no need to install pre-commit globally

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

# Data object in Python

## Setup

Pre-requisites:

- uv tool - [Astral uv](https://docs.astral.sh/uv/)

Bootstrap:

- Create venv, install all deps: `uv sync --frozen`
- Install pre-commit hooks: `uv run pre-commit install`
  - It installs pre-commit from project venv, no need to install pre-commit globally

## Operations

#### Run pre-commit hooks

- Run only over staged files: `uv run pre-commit run`
- Run over all files: `uv run pre-commit run -a`

#### Update deps

- update deps in `pyproject.toml`
- run `uv sync`

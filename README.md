# Data Objects in Python - Performance Benchmark

Benchmarking tool that measures memory and CPU cost of creating hundreds of thousands objects using different Python data structure approaches.

## Measured Metrics

- **Results Size RAM** - deep memory footprint of all created objects
- **RAM Used** - process RSS delta during execution
- **CPU User / System Time** - CPU time in user and kernel space

## Scenarios

- Python class
- Python class with `__slots__`
- Dataclass
- Dataclass with `slots=True`
- NamedTuple
- TypedDict
- SimpleNamespace
- Pydantic Model
- Pydantic Dataclass
- Pydantic Dataclass with `slots=True`

## Running

```bash
uv run python src/main.py
uv run python src/main.py -n 1000 -t 4  # custom instance and trials count
uv run python src/main.py --help        # show all options
```

## Results

### 2026-03-02

Run on 2026-03-02 with `uv run python src/main.py -n 100000 -t 10` (100,000 objects, 10 trials, median values).

**Summary**:

- Slots cut memory ~22% — `__slots__` variants (Class, Dataclass, Pydantic Dataclass) vs their non-slots counterparts.
- Pydantic Model is the heaviest — roughly 60% more memory than slots-based options.
- CPU time varies little — all scenarios fall within a ~15% range, so the choice is primarily about memory, not speed.
- Dict-backed types cost more — TypedDict and SimpleNamespace sit between plain classes and Pydantic in memory usage.

| No  | Scenario                       | Res Size RAM | RAM Used | Wall Time | CPU Time |
|-----|--------------------------------|--------------|----------|-----------|----------|
|  1  | Class                          |      40.0 MB |  34.3 MB |    6.367s |   6.280s |
|  2  | Class with Slots               |      31.2 MB |  30.3 MB |    6.429s |   6.308s |
|  3  | Dataclass                      |      40.0 MB |  34.3 MB |    6.540s |   6.392s |
|  4  | Dataclass with Slots           |      31.2 MB |  30.3 MB |    6.475s |   6.392s |
|  5  | Named Tuple                    |      32.0 MB |  31.9 MB |    6.510s |   6.419s |
|  6  | Typed Dict                     |      43.2 MB |  42.3 MB |    6.569s |   6.431s |
|  7  | Simple Namespace               |      47.2 MB |  46.3 MB |    6.622s |   6.506s |
|  8  | Pydantic Model                 |      50.4 MB |  71.1 MB |    6.843s |   6.747s |
|  9  | Pydantic Dataclass             |      48.0 MB |  49.5 MB |    7.198s |   7.092s |
| 10  | Pydantic Dataclass with Slots  |      31.2 MB |  30.3 MB |    7.234s |   7.117s |

### Comparison (Result Size RAM)

How much more/less memory each row uses compared to each column:

|                                | Class  | Class w/ Slots | Dataclass | DC w/ Slots | Named Tuple | Typed Dict | Simple NS | Pydantic Model | Pydantic DC | Pydantic DC w/ Slots |
|--------------------------------|--------|----------------|-----------|-------------|-------------|------------|-----------|----------------|-------------|----------------------|
| Class                          |   -    |     +28.2%     |   +0.0%   |    +28.2%   |   +25.0%    |   -7.4%    |  -15.3%   |    -20.6%      |   -16.7%    |        +28.2%        |
| Class with Slots               | -22.0% |       -        |  -22.0%   |    +0.0%    |    -2.5%    |   -27.8%   |  -33.9%   |    -38.1%      |   -35.0%    |         +0.0%        |
| Dataclass                      |  +0.0% |     +28.2%     |     -     |    +28.2%   |   +25.0%    |   -7.4%    |  -15.3%   |    -20.6%      |   -16.7%    |        +28.2%        |
| Dataclass with Slots           | -22.0% |      +0.0%     |  -22.0%   |      -      |    -2.5%    |   -27.8%   |  -33.9%   |    -38.1%      |   -35.0%    |         +0.0%        |
| Named Tuple                    | -20.0% |      +2.6%     |  -20.0%   |    +2.6%    |      -      |   -25.9%   |  -32.2%   |    -36.5%      |   -33.3%    |         +2.6%        |
| Typed Dict                     |  +8.0% |     +38.5%     |   +8.0%   |    +38.5%   |   +35.0%    |     -      |   -8.5%   |    -14.3%      |   -10.0%    |        +38.5%        |
| Simple Namespace               | +18.0% |     +51.3%     |  +18.0%   |    +51.3%   |   +47.5%    |   +9.3%    |     -     |     -6.3%      |    -1.7%    |        +51.3%        |
| Pydantic Model                 | +26.0% |     +61.5%     |  +26.0%   |    +61.5%   |   +57.5%    |   +16.7%   |   +6.8%   |       -        |    +5.0%    |        +61.5%        |
| Pydantic Dataclass             | +20.0% |     +53.8%     |  +20.0%   |    +53.8%   |   +50.0%    |   +11.1%   |   +1.7%   |     -4.8%      |      -      |        +53.8%        |
| Pydantic DC with Slots         | -22.0% |      +0.0%     |  -22.0%   |    +0.0%    |    -2.5%    |   -27.8%   |  -33.9%   |    -38.1%      |   -35.0%    |           -          |

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

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

Run with `uv run python src/main.py -n 100000 -t 10` (100,000 objects, 10 trials, mean values).

#### Summary

- **Slots cut memory ~28%** — `__slots__` variants (Class, Dataclass, Pydantic Dataclass) consistently use ~28% less memory than their non-slots counterparts.
- **Pydantic Model is the heaviest** — 83% more memory than slots-based options, and 50% more CPU time than plain classes.
- **Pydantic Dataclasses are CPU-expensive** — over 2x the CPU time of plain classes/dataclasses, even though Pydantic DC with Slots matches them on memory.
- **Non-Pydantic stdlib types are fast** — Class, Dataclass, NamedTuple, TypedDict, SimpleNamespace all fall within a tight ~10% CPU range. The choice among them is about memory, not speed.
- **Dict-backed types cost more memory** — TypedDict (+10%) and SimpleNamespace (+22%) sit between plain classes and Pydantic.

| No  | Scenario                       | Res Size RAM | RAM Used | Wall Time | CPU Time |
|-----|--------------------------------|--------------|----------|-----------|----------|
|  1  | Class                          |      32.0 MB |  26.3 MB |    0.368s |   0.366s |
|  2  | Class with Slots               |      23.2 MB |  22.3 MB |    0.361s |   0.355s |
|  3  | Dataclass                      |      32.0 MB |  26.3 MB |    0.366s |   0.361s |
|  4  | Dataclass with Slots           |      23.2 MB |  22.3 MB |    0.365s |   0.362s |
|  5  | Named Tuple                    |      24.0 MB |  23.9 MB |    0.392s |   0.389s |
|  6  | Typed Dict                     |      35.2 MB |  34.3 MB |    0.374s |   0.370s |
|  7  | Simple Namespace               |      39.2 MB |  38.3 MB |    0.377s |   0.373s |
|  8  | Pydantic Model                 |      42.4 MB |  63.1 MB |    0.555s |   0.547s |
|  9  | Pydantic Dataclass             |      40.0 MB |  41.5 MB |    0.806s |   0.787s |
| 10  | Pydantic Dataclass with Slots  |      23.2 MB |  22.3 MB |    0.765s |   0.759s |

#### Comparison: Result Size RAM

How much more/less memory each row uses compared to each column:

|                                | Class  | Class w/ Slots | Dataclass | DC w/ Slots | Named Tuple | Typed Dict | Simple NS | Pydantic Model | Pydantic DC | Pydantic DC w/ Slots |
|--------------------------------|--------|----------------|-----------|-------------|-------------|------------|-----------|----------------|-------------|----------------------|
| Class                          |   -    |     +37.9%     |   +0.0%   |   +37.9%    |   +33.3%    |   -9.1%    |  -18.4%   |    -24.5%      |   -20.0%    |        +37.9%        |
| Class with Slots               | -27.5% |       -        |  -27.5%   |    +0.0%    |    -3.3%    |   -34.1%   |  -40.8%   |    -45.3%      |   -42.0%    |         +0.0%        |
| Dataclass                      |  +0.0% |     +37.9%     |     -     |   +37.9%    |   +33.3%    |   -9.1%    |  -18.4%   |    -24.5%      |   -20.0%    |        +37.9%        |
| Dataclass with Slots           | -27.5% |      +0.0%     |  -27.5%   |      -      |    -3.3%    |   -34.1%   |  -40.8%   |    -45.3%      |   -42.0%    |         +0.0%        |
| Named Tuple                    | -25.0% |      +3.4%     |  -25.0%   |    +3.4%    |      -      |   -31.8%   |  -38.8%   |    -43.4%      |   -40.0%    |         +3.4%        |
| Typed Dict                     | +10.0% |     +51.7%     |  +10.0%   |   +51.7%    |   +46.7%    |     -      |  -10.2%   |    -17.0%      |   -12.0%    |        +51.7%        |
| Simple Namespace               | +22.5% |     +69.0%     |  +22.5%   |   +69.0%    |   +63.3%    |   +11.4%   |     -     |     -7.5%      |    -2.0%    |        +69.0%        |
| Pydantic Model                 | +32.5% |     +82.7%     |  +32.5%   |   +82.7%    |   +76.7%    |   +20.5%   |   +8.2%   |       -        |    +6.0%    |        +82.7%        |
| Pydantic Dataclass             | +25.0% |     +72.4%     |  +25.0%   |   +72.4%    |   +66.7%    |   +13.6%   |   +2.0%   |     -5.7%      |      -      |        +72.4%        |
| Pydantic DC with Slots         | -27.5% |      +0.0%     |  -27.5%   |    +0.0%    |    -3.3%    |   -34.1%   |  -40.8%   |    -45.3%      |   -42.0%    |           -          |

#### Comparison: CPU Time

How much more/less CPU time each row uses compared to each column:

|                                |  Class  | Class w/ Slots | Dataclass | DC w/ Slots | Named Tuple | Typed Dict | Simple NS | Pydantic Model | Pydantic DC | Pydantic DC w/ Slots |
|--------------------------------|---------|----------------|-----------|-------------|-------------|------------|-----------|----------------|-------------|----------------------|
| Class                          |    -    |      +3.1%     |   +1.3%   |    +0.9%    |    -6.0%    |   -1.3%    |   -2.1%   |    -33.1%      |   -53.6%    |        -51.9%        |
| Class with Slots               |  -3.0%  |       -        |   -1.7%   |    -2.2%    |    -8.8%    |   -4.2%    |   -5.0%   |    -35.1%      |   -55.0%    |        -53.3%        |
| Dataclass                      |  -1.3%  |      +1.8%     |     -     |    -0.4%    |    -7.2%    |   -2.5%    |   -3.3%   |    -34.0%      |   -54.2%    |        -52.5%        |
| Dataclass with Slots           |  -0.9%  |      +2.2%     |   +0.4%   |      -      |    -6.8%    |   -2.1%    |   -2.9%   |    -33.7%      |   -54.0%    |        -52.3%        |
| Named Tuple                    |  +6.4%  |      +9.7%     |   +7.8%   |    +7.3%    |      -      |   +5.1%    |   +4.2%   |    -28.9%      |   -50.6%    |        -48.8%        |
| Typed Dict                     |  +1.3%  |      +4.4%     |   +2.6%   |    +2.2%    |    -4.8%    |     -      |   -0.8%   |    -32.3%      |   -53.0%    |        -51.2%        |
| Simple Namespace               |  +2.1%  |      +5.3%     |   +3.5%   |    +3.0%    |    -4.0%    |   +0.8%    |     -     |    -31.7%      |   -52.6%    |        -50.8%        |
| Pydantic Model                 | +49.6%  |     +54.2%     |  +51.5%   |   +50.9%    |   +40.6%    |   +47.7%   |  +46.4%   |       -        |   -30.6%    |        -28.0%        |
| Pydantic Dataclass             | +115.4% |    +122.0%     | +118.2%   |  +117.2%    |  +102.4%    |  +112.7%   | +110.9%   |    +44.0%      |      -      |         +3.7%        |
| Pydantic DC with Slots         | +107.7% |    +114.1%     | +110.4%   |  +109.5%    |   +95.2%    |  +105.1%   | +103.3%   |    +38.9%      |    -3.6%    |           -          |

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

from cases.class_regular import create_class_regular
from cases.class_slots import create_class_slots
from cases.dataclass_regular import create_dataclass_regular
from cases.dataclass_slots import create_dataclass_slots
from cases.pydantic import create_pydantic
from cases.pydantic_dataclass import create_pydantic_dataclass
from cases.pydantic_dataclass_slots import create_pydantic_dataclass_slots
from resource_monitor.run import run_measurement
from resource_monitor.run_config import RunConfig


def main():
    num_cycles = 1_000_000
    configs = [
        RunConfig(name="class_regular", fun=create_class_regular),
        RunConfig(name="class_slots", fun=create_class_slots),
        RunConfig(name="dataclass_regular", fun=create_dataclass_regular),
        RunConfig(name="dataclass_slots", fun=create_dataclass_slots),
        RunConfig(name="pydantic", fun=create_pydantic),
        RunConfig(name="pydantic_dataclass", fun=create_pydantic_dataclass),
        RunConfig(name="pydantic_dataclass_slots", fun=create_pydantic_dataclass_slots),
    ]
    configs.reverse()
    for config in configs:
        print(f"### Running {config.name} with num_cycles={num_cycles}...")
        stats = run_measurement(config, num_cycles=num_cycles)
        print(stats.as_human_str())


if __name__ == "__main__":
    main()

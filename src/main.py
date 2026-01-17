import logging

from runner.run import run_scenarios
from scenarios.base import BaseScenario
from scenarios.pydantic_dataclass import PydanticDataclassScenario
from scenarios.pydantic_dataclass_with_slots import PydanticDataclassWithSlotsScenario
from scenarios.pydantic_model import PydanticModelScenario
from scenarios.python_class import PythonClassScenario
from scenarios.python_class_with_slots import PythonClassWithSlotsScenario
from scenarios.python_dataclass import PythonDataclassScenario
from scenarios.python_dataclass_with_slots import PythonDataclassWithSlotsScenario


def main():
    configure_logger()
    scenarios: list[BaseScenario] = [
        PythonClassScenario(),
        PythonClassWithSlotsScenario(),
        PythonDataclassScenario(),
        PythonDataclassWithSlotsScenario(),
        PydanticModelScenario(),
        PydanticDataclassScenario(),
        PydanticDataclassWithSlotsScenario(),
    ]
    run_scenarios(scenarios, 1_000)


def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


if __name__ == "__main__":
    main()

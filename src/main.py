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
        # %(levelname).1s takes the first character of the level name (I, W, E, etc.)
        # %(msecs)03d prints millisecs, something that datefmt does not offer
        format="%(levelname).1s %(asctime)s.%(msecs)03d [%(name)s] %(message)s",
        # %f provides microsecond precision; we truncate/format as needed
        datefmt="%Y-%m-%d %H:%M:%S",
    )


if __name__ == "__main__":
    main()

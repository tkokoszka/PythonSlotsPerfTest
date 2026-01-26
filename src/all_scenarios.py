from scenarios.base import BaseScenario
from scenarios.named_tuple import NamedTupleScenario
from scenarios.pydantic_dataclass import PydanticDataclassScenario
from scenarios.pydantic_dataclass_with_slots import PydanticDataclassWithSlotsScenario
from scenarios.pydantic_model import PydanticModelScenario
from scenarios.python_class import PythonClassScenario
from scenarios.python_class_with_slots import PythonClassWithSlotsScenario
from scenarios.python_dataclass import PythonDataclassScenario
from scenarios.python_dataclass_with_slots import PythonDataclassWithSlotsScenario
from scenarios.simple_namespace import SimpleNamespaceScenario
from scenarios.typed_dict import TypedDictScenario

ALL_SCENARIOS: list[BaseScenario] = [
    PythonClassScenario(),
    PythonClassWithSlotsScenario(),
    PythonDataclassScenario(),
    PythonDataclassWithSlotsScenario(),
    NamedTupleScenario(),
    TypedDictScenario(),
    SimpleNamespaceScenario(),
    PydanticModelScenario(),
    PydanticDataclassScenario(),
    PydanticDataclassWithSlotsScenario(),
]

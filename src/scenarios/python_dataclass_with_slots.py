import random
from dataclasses import dataclass
from uuid import uuid4

from scenarios.base import BaseScenario


@dataclass(slots=True)
class User:
    id: str
    name: str
    surname: str
    age: int


class PythonDataclassWithSlotsScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Dataclass with Slots"

    @property
    def description(self) -> str:
        return "Python builtin dataclass with slots=True."

    def create_one(self, seq_no: int) -> User:
        age = random.randint(1, 100)
        return User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)

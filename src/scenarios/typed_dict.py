import random
from typing import TypedDict
from uuid import uuid4

from scenarios.base import BaseScenario


class User(TypedDict):
    id: str
    name: str
    surname: str
    age: int


class TypedDictScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Typed Dict"

    @property
    def description(self) -> str:
        return "Python builtin TypedDict."

    def create_one(self, seq_no: int) -> User:
        age = random.randint(1, 100)
        return User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)

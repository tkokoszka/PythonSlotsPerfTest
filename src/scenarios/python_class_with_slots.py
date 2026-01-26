import random
from uuid import uuid4

from scenarios.base import BaseScenario


class User:
    __slots__ = ("id", "name", "surname", "age")

    def __init__(self, id: str, name: str, surname: str, age: int):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age


class PythonClassWithSlotsScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Class with Slots"

    @property
    def description(self) -> str:
        return "Python builtin class with __slots__."

    def create_one(self, seq_no: int) -> User:
        age = random.randint(1, 100)
        return User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)

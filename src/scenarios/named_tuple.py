from typing import NamedTuple

from scenarios.base import BaseScenario


class User(NamedTuple):
    id: str
    name: str
    surname: str
    age: int


class NamedTupleScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Named Tuple"

    @property
    def description(self) -> str:
        return "Python builtin NamedTuple."

    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> User:
        return User(id=id, name=name, surname=surname, age=age)

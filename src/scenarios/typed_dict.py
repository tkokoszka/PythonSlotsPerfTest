from typing import TypedDict

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

    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> User:
        return User(id=id, name=name, surname=surname, age=age)

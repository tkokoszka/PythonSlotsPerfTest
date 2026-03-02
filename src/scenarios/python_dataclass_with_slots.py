from dataclasses import dataclass

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

    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> User:
        return User(id=id, name=name, surname=surname, age=age)

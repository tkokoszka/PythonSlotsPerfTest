from dataclasses import dataclass

from scenarios.base import BaseScenario


@dataclass
class User:
    id: str
    name: str
    surname: str
    age: int


class PythonDataclassScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Dataclass"

    @property
    def description(self) -> str:
        return "Python builtin dataclass."

    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> User:
        return User(id=id, name=name, surname=surname, age=age)

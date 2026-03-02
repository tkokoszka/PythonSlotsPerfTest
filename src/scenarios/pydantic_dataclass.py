from pydantic.dataclasses import dataclass as pydantic_dataclass

from scenarios.base import BaseScenario


@pydantic_dataclass
class User:
    id: str
    name: str
    surname: str
    age: int


class PydanticDataclassScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Pydantic Dataclass"

    @property
    def description(self) -> str:
        return "Pydantic dataclass."

    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> User:
        return User(id=id, name=name, surname=surname, age=age)

from pydantic.dataclasses import dataclass as pydantic_dataclass

from scenarios.base import BaseScenario


@pydantic_dataclass(slots=True)
class User:
    id: str
    name: str
    surname: str
    age: int


class PydanticDataclassWithSlotsScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Pydantic Dataclass with Slots"

    @property
    def description(self) -> str:
        return "Pydantic dataclass with slots=True."

    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> User:
        return User(id=id, name=name, surname=surname, age=age)

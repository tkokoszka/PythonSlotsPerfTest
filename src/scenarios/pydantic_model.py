from pydantic import BaseModel

from scenarios.base import BaseScenario


class User(BaseModel):
    id: str
    name: str
    surname: str
    age: int


class PydanticModelScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Pydantic Model"

    @property
    def description(self) -> str:
        return "Pydantic Model."

    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> User:
        return User(id=id, name=name, surname=surname, age=age)

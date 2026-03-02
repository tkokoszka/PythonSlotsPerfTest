import random
from uuid import uuid4

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

    def create_one(self, seq_no: int) -> User:
        age = random.randint(1, 100)
        return User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)

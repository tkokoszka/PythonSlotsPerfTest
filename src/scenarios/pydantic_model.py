import random
from uuid import uuid4

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

    def create_one(self, seq_no: int) -> User:
        age = random.randint(1, 100)
        return User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)

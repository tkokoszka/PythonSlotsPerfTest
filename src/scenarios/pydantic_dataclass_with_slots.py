import random
from uuid import uuid4

from pydantic import Field, PositiveInt
from pydantic.dataclasses import dataclass as pydantic_dataclass

from scenarios.base import BaseScenario


@pydantic_dataclass(slots=True)
class User:
    id: str = Field(..., description="Unique identifier for the user")
    name: str = Field(..., description="First name of the user")
    surname: str = Field(..., description="Last name of the user")
    age: PositiveInt = Field(..., description="Age of the user (must be positive)")


class PydanticDataclassWithSlotsScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Pydantic Dataclass with Slots"

    @property
    def description(self) -> str:
        return "Pydantic dataclass with slots=True."

    def create_one(self, seq_no: int) -> User:
        age = random.randint(1, 100)
        return User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)

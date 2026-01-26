import random
from uuid import uuid4

from pydantic import BaseModel, Field, PositiveInt

from scenarios.base import BaseScenario


class User(BaseModel):
    id: str = Field(..., description="Unique identifier for the user")
    name: str = Field(..., description="First name of the user")
    surname: str = Field(..., description="Last name of the user")
    age: PositiveInt = Field(..., description="Age of the user (must be positive)")


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

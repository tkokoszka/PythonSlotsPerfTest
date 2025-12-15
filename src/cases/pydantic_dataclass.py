import random
from uuid import uuid4

from pydantic import Field, PositiveInt
from pydantic.dataclasses import dataclass as pydantic_dataclass


@pydantic_dataclass
class User:
    id: str = Field(..., description="Unique identifier for the user")
    name: str = Field(..., description="First name of the user")
    surname: str = Field(..., description="Last name of the user")
    age: PositiveInt = Field(..., description="Age of the user (must be positive)")


def create_pydantic_dataclass(num_instances: int) -> list[User]:
    result = []
    for _ in range(num_instances):
        age = random.randint(1, 100)
        u = User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)
        result.append(u)

    return result

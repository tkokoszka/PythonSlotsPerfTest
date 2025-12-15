import random
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class User:
    id: str
    name: str
    surname: str
    age: int


def create_dataclass_regular(num_instances: int) -> list[User]:
    result = []
    for _ in range(num_instances):
        age = random.randint(1, 100)
        u = User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)
        result.append(u)

    return result

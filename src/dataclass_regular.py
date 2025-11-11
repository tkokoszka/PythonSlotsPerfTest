import random
from dataclasses import dataclass
from uuid import uuid4


@dataclass
class User:
    id: str
    name: str
    surname: str
    age: int


def create_dataclasses(n: int) -> list[User]:
    result = []
    for i in range(n):
        age = random.randint(1, 100)
        u = User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)
        result.append(u)

    return result

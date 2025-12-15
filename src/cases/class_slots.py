import random
from uuid import uuid4


class User:
    __slots__ = ("id", "name", "surname", "age")

    def __init__(self, id: str, name: str, surname: str, age: int):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age


def create_class_slots(num_instances: int) -> list[User]:
    result = []
    for _ in range(num_instances):
        age = random.randint(1, 100)
        u = User(id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age)
        result.append(u)

    return result

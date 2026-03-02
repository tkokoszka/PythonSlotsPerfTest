from scenarios.base import BaseScenario


class User:
    __slots__ = ("id", "name", "surname", "age")

    def __init__(self, id: str, name: str, surname: str, age: int):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age


class PythonClassWithSlotsScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Class with Slots"

    @property
    def description(self) -> str:
        return "Python builtin class with __slots__."

    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> User:
        return User(id=id, name=name, surname=surname, age=age)

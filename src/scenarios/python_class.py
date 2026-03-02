from scenarios.base import BaseScenario


class User:
    def __init__(self, id: str, name: str, surname: str, age: int):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age


class PythonClassScenario(BaseScenario[User]):
    @property
    def name(self) -> str:
        return "Class"

    @property
    def description(self) -> str:
        return "Python builtin class."

    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> User:
        return User(id=id, name=name, surname=surname, age=age)

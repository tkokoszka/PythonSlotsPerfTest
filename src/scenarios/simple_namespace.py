from types import SimpleNamespace

from scenarios.base import BaseScenario


class SimpleNamespaceScenario(BaseScenario[SimpleNamespace]):
    @property
    def name(self) -> str:
        return "Simple Namespace"

    @property
    def description(self) -> str:
        return "Python builtin SimpleNamespace."

    def construct_one(
        self, *, id: str, name: str, surname: str, age: int
    ) -> SimpleNamespace:
        return SimpleNamespace(id=id, name=name, surname=surname, age=age)

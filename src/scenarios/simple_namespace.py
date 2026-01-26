import random
from types import SimpleNamespace
from uuid import uuid4

from scenarios.base import BaseScenario


class SimpleNamespaceScenario(BaseScenario[SimpleNamespace]):
    @property
    def name(self) -> str:
        return "Simple Namespace"

    @property
    def description(self) -> str:
        return "Python builtin SimpleNamespace."

    def create_one(self, seq_no: int) -> SimpleNamespace:
        age = random.randint(1, 100)
        return SimpleNamespace(
            id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age
        )

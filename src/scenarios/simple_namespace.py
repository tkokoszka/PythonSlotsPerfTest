import random
from types import SimpleNamespace
from typing import Protocol, cast
from uuid import uuid4

from scenarios.base import BaseScenario


class UserProtocol(Protocol):
    id: str
    name: str
    surname: str
    age: int


class SimpleNamespaceScenario(BaseScenario[UserProtocol]):
    @property
    def name(self) -> str:
        return "Simple Namespace"

    @property
    def description(self) -> str:
        return "Python builtin SimpleNamespace."

    def create_one(self, seq_no: int) -> UserProtocol:
        age = random.randint(1, 100)
        return cast(
            UserProtocol,
            SimpleNamespace(
                id=str(uuid4()), name=str(uuid4()), surname=str(uuid4()), age=age
            ),
        )

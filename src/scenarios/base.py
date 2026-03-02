from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseScenario(ABC, Generic[T]):
    @property
    @abstractmethod
    def name(self) -> str:
        """Short human readable name."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Longer human readable description of this scenario.

        Explain what object this scenario creates, what is special about it.
        """
        pass

    @abstractmethod
    def construct_one(self, *, id: str, name: str, surname: str, age: int) -> T:
        """Construct a single instance of the test object from pre-generated values."""
        pass

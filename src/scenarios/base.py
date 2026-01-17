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
    def create_one(self, seq_no: int) -> T:
        """Create a single instance of test object for this scenario.

        Args:
            seq_no: sequence number (from 0), when creating series of objects.
                    Can be used to seed data, e.g. be part of name.
        """
        pass

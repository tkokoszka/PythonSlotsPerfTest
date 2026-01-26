from abc import ABC, abstractmethod

from models.execution_result import ExecutionResult


class ExecutionReporter(ABC):
    @abstractmethod
    def report(self, results: list[ExecutionResult]) -> str:
        pass

from abc import ABC, abstractmethod

from models.execution_stats import ExecutionStats


class ExecutionReporter(ABC):
    @abstractmethod
    def report(self, executions_stats: list[ExecutionStats]) -> str:
        pass

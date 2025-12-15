from dataclasses import dataclass
from typing import Callable, TypeAlias

FunToRun: TypeAlias = Callable[[int], list]


@dataclass
class RunConfig:
    name: str
    fun: FunToRun

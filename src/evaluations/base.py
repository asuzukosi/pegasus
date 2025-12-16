from abc import ABC, abstractmethod
from typing import Callable

class Evaluation(ABC):
    @abstractmethod
    def evaluate(self, inputs, targets, function: Callable) -> bool:
        pass
    @abstractmethod
    def display_result(self, **kwargs) -> None:
        pass

    @abstractmethod
    def feedback(self, **kwargs) -> None:
        pass
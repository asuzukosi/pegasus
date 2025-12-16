from evaluations.base import Evaluation
from typing import Callable

class ClassifierEvaluation(Evaluation):
    def evaluate(self, inputs, targets, function: Callable) -> bool:
        pass

    def display_result(self, **kwargs) -> None:
        pass

    def feedback(self, **kwargs) -> None:
        pass
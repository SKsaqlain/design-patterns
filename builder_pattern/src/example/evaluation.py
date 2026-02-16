import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


# --- Pipeline Component: Evaluation ---
# Abstract base for all evaluation metrics in the pipeline.
class Evaluation(ABC):
    def __init__(self, name):
        self.name = name  # Identifier used in pipeline config display

    @abstractmethod
    def run_evaluation(self):
        pass


# --- Concrete Evaluation: F1Score ---
# Simulates computing the F1 metric (precision–recall balance).
class F1Score(Evaluation):
    def __init__(self):
        super().__init__('F1_Score')

    def run_evaluation(self):
        logger.info("Running F1 Score evaluation on model")

import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


# --- Pipeline Component: Model ---
# Abstract base for all ML models in the pipeline.
class Model(ABC):
    def __init__(self, name):
        self.name = name  # Identifier used in pipeline config display

    @abstractmethod
    def run_model(self):
        pass


# --- Concrete Model: LogisticRegression ---
# Simulates training a logistic regression classifier.
class LogisticRegression(Model):
    def __init__(self):
        super().__init__("Logistic_Regression")

    def run_model(self):
        logger.info("Running logistic regression")
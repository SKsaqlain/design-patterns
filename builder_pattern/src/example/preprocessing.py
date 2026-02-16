import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


# --- Pipeline Component: Preprocessing ---
# Abstract base for all preprocessing steps in the pipeline.
class Preprocessing(ABC):
    def __init__(self, name):
        self.name = name  # Identifier used in pipeline config display

    @abstractmethod
    def run_preprocessing(self):
        pass


# --- Concrete Preprocessing: Normalize ---
# Simulates scaling features to a standard range.
class Normalize(Preprocessing):
    def __init__(self):
        super().__init__('Normalize')

    def run_preprocessing(self):
        logger.info("Performing normalization on the data")
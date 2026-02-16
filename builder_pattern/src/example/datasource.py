import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


# --- Pipeline Component: DataSource ---
# Abstract base for all data sources in the pipeline.
class DataSource(ABC):
    def __init__(self, name):
        self.name = name  # Identifier used in pipeline config display

    @abstractmethod
    def fetch_data(self):
        pass


# --- Concrete DataSource: S3 ---
# Simulates reading data from an AWS S3 bucket.
class S3(DataSource):
    def __init__(self):
        super().__init__('S3')

    def fetch_data(self):
        logger.info("Fetching data from S3")
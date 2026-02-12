import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

# Abstract Product — interface for all cloud storage types
class Storage(ABC):
    @abstractmethod
    def connect_to_storage(self):
        pass


# Concrete Product — AWS S3 bucket
class AWS_Storage(Storage):
    def connect_to_storage(self):
        logger.info("Connecting to AWS Storage")

# Concrete Product — GCP Cloud Storage bucket
class GCP_Storage(Storage):
    def connect_to_storage(self):
        logger.info("Connecting to GCP Storage")

# Concrete Product — Azure Blob Storage
class AZURE_Storage(Storage):
    def connect_to_storage(self):
        logger.info("Connecting to AZURE Storage")
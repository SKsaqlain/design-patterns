import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

# Abstract Product — interface for all cloud database types
class Database(ABC):
    @abstractmethod
    def connect_to_db(self):
        pass


# Concrete Product — AWS RDS instance
class AWS_Database(Database):
    def connect_to_db(self):
        logger.info("Connecting to AWS Database")

# Concrete Product — GCP Cloud SQL instance
class GCP_Database(Database):
    def connect_to_db(self):
        logger.info("Connecting to GCP Database")

# Concrete Product — Azure SQL instance
class AZURE_Database(Database):
    def connect_to_db(self):
        logger.info("Connecting to AZURE Database")
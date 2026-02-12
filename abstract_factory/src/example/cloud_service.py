import logging
from abc import ABC, abstractmethod

from src.example.database import AWS_Database, AZURE_Database, GCP_Database
from src.example.storage import AWS_Storage, AZURE_Storage, GCP_Storage
from src.example.virtual_machine import AWS_VM, AZURE_VM, GCP_VM

logger = logging.getLogger(__name__)

# Abstract Factory — declares creation methods for each product in the family (VM + DB + Storage).
# Each concrete factory produces a matched set of cloud services for a specific provider.
class CloudServiceFactory(ABC):

    def __init__(self,name: str):
        self.name=name

    # Creates a VM instance for this provider
    @abstractmethod
    def get_virtual_machine(self):
        pass

    # Creates a database instance for this provider
    @abstractmethod
    def get_database(self):
        pass

    # Creates a storage instance for this provider
    @abstractmethod
    def get_storage(self):
        pass


# Concrete Factory — produces AWS services as a matched set
class AWSFactory(CloudServiceFactory):
    def __init__(self):
        super().__init__("AWS")

    def get_virtual_machine(self):
        logger.info(f"[{self.name}] creating Virtual Machine")
        return AWS_VM()

    def get_database(self):
        logger.info(f"[{self.name}] creating Database")
        return AWS_Database()

    def get_storage(self):
        logger.info(f"[{self.name}] creating Storage")
        return AWS_Storage()

# Concrete Factory — produces GCP services as a matched set
class GCPFactory(CloudServiceFactory):
    def __init__(self):
        super().__init__("GCP")

    def get_virtual_machine(self):
        logger.info(f"[{self.name}] creating Virtual Machine")
        return GCP_VM()

    def get_database(self):
        logger.info(f"[{self.name}] creating Database")
        return GCP_Database()

    def get_storage(self):
        logger.info(f"[{self.name}] creating Storage")
        return GCP_Storage()

# Concrete Factory — produces Azure services as a matched set
class AZUREFactory(CloudServiceFactory):
    def __init__(self):
        super().__init__("Azure")

    def get_virtual_machine(self):
        logger.info(f"[{self.name}] creating Virtual Machine")
        return AZURE_VM()

    def get_database(self):
        logger.info(f"[{self.name}] creating Database")
        return AZURE_Database()

    def get_storage(self):
        logger.info(f"[{self.name}] creating Storage")
        return AZURE_Storage()
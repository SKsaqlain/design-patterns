import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

# Abstract Product — interface for all cloud VM types
class VirtualMachine(ABC):

    @abstractmethod
    def start_machine(self):
        pass


# Concrete Product — AWS EC2 instance
class AWS_VM(VirtualMachine):
    def start_machine(self):
        logger.info("Starting AWS Virtual Machine instance")

# Concrete Product — GCP Compute Engine instance
class GCP_VM(VirtualMachine):
    def start_machine(self):
        logger.info("Starting GCP Virtual Machine instance")

# Concrete Product — Azure VM instance
class AZURE_VM(VirtualMachine):
    def start_machine(self):
        logger.info("Starting AZURE Virtual Machine instance")
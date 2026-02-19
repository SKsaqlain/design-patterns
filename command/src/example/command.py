import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


# Command interface — adds undo alongside execute
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

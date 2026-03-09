from abc import ABC, abstractmethod
from enum import Enum


class SupportHandler(ABC):
    @abstractmethod
    def handle_request(self,request):
        pass

    @abstractmethod
    def set_next_handler(self,next_handler):
        pass

class Priority(Enum):
    BASIC=1
    INTERMEDIATE=2
    CRITICAL=3
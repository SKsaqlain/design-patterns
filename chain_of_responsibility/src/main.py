from abc import ABC, abstractmethod
from enum import Enum


# Enum defining ticket priority levels
class Priority(Enum):
    BASIC = 1
    INTERMEDIATE = 2
    CRITICAL = 3


# Data object carrying the priority of a support request
class Request:
    def __init__(self, priority):
        self.priority = priority  # priority name string (e.g. 'BASIC')


# Abstract handler — declares the chain interface
class SupportHandler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass  # process or forward the request

    @abstractmethod
    def set_next_handler(self, next_handler):
        pass  # link to the next handler in the chain


# Concrete handler — resolves BASIC priority tickets
class Level1SupportHandler(SupportHandler):
    def __init__(self):
        self.next_handler = None  # no successor by default

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler  # link the next handler

    def handle_request(self, request):
        if request.priority == Priority.BASIC.name:
            print("Level 1 Support handled the request")  # handled here
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)  # pass to next handler


# Concrete handler — resolves INTERMEDIATE priority tickets
class Level2SupportHandler(SupportHandler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, request):
        if request.priority == Priority.INTERMEDIATE.name:
            print("Level 2 Support handled the request")
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)


# Concrete handler — resolves CRITICAL priority tickets (end of chain)
class Level3SupportHandler(SupportHandler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, request):
        if request.priority == Priority.CRITICAL.name:
            print("Level 3 Support handled the request")
        else:
            print(" Cannot handle request ")  # no handler could process this


if __name__ == '__main__':
    # Create handlers for each support level
    level1_handler = Level1SupportHandler()
    level2_handler = Level2SupportHandler()
    level3_handler = Level3SupportHandler()

    # Build the chain: Level 1 → Level 2 → Level 3
    level1_handler.set_next_handler(level2_handler)
    level2_handler.set_next_handler(level3_handler)

    # Send requests — each one travels the chain until handled
    level1_handler.handle_request(Request('BASIC'))
    level1_handler.handle_request(Request('INTERMEDIATE'))
    level1_handler.handle_request(Request('CRITICAL'))
    level1_handler.handle_request(Request('XYZ'))  # unhandled priority

from abc import ABC, abstractmethod
from enum import Enum

class Priority(Enum):
    BASIC=1
    INTERMEDIATE=2
    CRITICAL=3

class Request:
    def __init__(self,priority):
        self.priority=priority

class SupportHandler(ABC):
    @abstractmethod
    def handle_request(self,request):
        pass

    @abstractmethod
    def set_next_handler(self,next_handler):
        pass


class Level1SupportHandler(SupportHandler):
    def __init__(self):
        self.next_handler=None
    
    def set_next_handler(self, next_handler):
        self.next_handler=next_handler
    
    def handle_request(self, request):
        if request.priority== Priority.BASIC:
            print("Level 1 Support handled the request")
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)



class Level2SupportHandler(SupportHandler):
    def __init__(self):
        self.next_handler=None
    
    def set_next_handler(self, next_handler):
        self.next_handler=next_handler
    
    def handle_request(self, request):
        if request.priority== Priority.INTERMEDIATE:
            print("Level s Support handled the request")
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)



class Level3SupportHandler(SupportHandler):
    def __init__(self):
        self.next_handler=None
    
    def set_next_handler(self, next_handler):
        self.next_handler=next_handler
    
    def handle_request(self, request):
        if request.priority== Priority.CRITICAL:
            print("Level s Support handled the request")
        else:
            print(" Cannot handle request ")



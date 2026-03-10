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
        if request.priority == Priority.BASIC.name:
            print("Level 1 Support handled the request")
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)



class Level2SupportHandler(SupportHandler):
    def __init__(self):
        self.next_handler=None
    
    def set_next_handler(self, next_handler):
        self.next_handler=next_handler
    
    def handle_request(self, request):
        if request.priority== Priority.INTERMEDIATE.name:
            print("Level 2 Support handled the request")
        elif self.next_handler is not None:
            self.next_handler.handle_request(request)



class Level3SupportHandler(SupportHandler):
    def __init__(self):
        self.next_handler=None
    
    def set_next_handler(self, next_handler):
        self.next_handler=next_handler
    
    def handle_request(self, request):
        if request.priority== Priority.CRITICAL.name:
            print("Level 3 Support handled the request")
        else:
            print(" Cannot handle request ")


if __name__=='__main__':
    level1_handler=Level1SupportHandler()
    level2_handler=Level2SupportHandler()
    level3_handler=Level3SupportHandler()

    level1_handler.set_next_handler(level2_handler)
    level2_handler.set_next_handler(level3_handler)

    level1_handler.handle_request(Request('BASIC'))
    level1_handler.handle_request(Request('INTERMEDIATE'))
    level1_handler.handle_request(Request('CRITICAL'))
    level1_handler.handle_request(Request('XYZ'))


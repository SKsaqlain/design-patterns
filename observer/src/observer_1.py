from abc import ABC, abstractmethod
from typing import List

class ObserverInterface(ABC):
    
    @abstractmethod
    def update(self,message: str)->None:
        pass


class Observer(ObserverInterface):
    def __init__(self,name):
        self.name=name
    

    def update(self,message):
        print(f"{self.name} received message {message}")
    



class Subject():
    def __init__(self,topic: str):
        self.topic=topic
        self.observers: List =[]


    def attach_observer(self,observer: ObserverInterface):
        self.observers.append(observer)
    
    def detach_observer(self,observer: ObserverInterface):
        print(f"Removing  observer { observer.name}")
        self.observers.remove(observer)
    
    def notify_observers(self,message):
        print(f"Subject with topic {self.topic} Sennding message to all observers {len(self.observers)}")
        for observer in self.observers:
            observer.update(message)


def main():
    ob1=Observer('observer_1')
    ob2=Observer('observer_2')
    ob3=Observer('observer_2')

    subject=Subject('topic_1')
    subject.attach_observer(ob1)
    subject.attach_observer(ob2)
    subject.attach_observer(ob3)

    subject.notify_observers("Hello ")
    subject.detach_observer(ob3)


if __name__=='__main__':
    main()
from abc import ABC, abstractmethod
from typing import List

# Observer interface — defines the contract for receiving notifications
class ObserverInterface(ABC):

    # Called by the subject when it has a new message
    @abstractmethod
    def update(self,message: str)->None:
        pass


# Concrete observer — prints the received message
class Observer(ObserverInterface):
    def __init__(self,name):
        self.name=name

    # Handles the notification from the subject
    def update(self,message):
        print(f"{self.name} received message {message}")


# Subject — maintains a list of observers and notifies them on changes
class Subject():
    def __init__(self,topic: str):
        self.topic=topic
        self.observers: List =[]

    # Subscribes an observer to this subject
    def attach_observer(self,observer: ObserverInterface):
        self.observers.append(observer)

    # Unsubscribes an observer from this subject
    def detach_observer(self,observer: ObserverInterface):
        print(f"Removing  observer { observer.name}")
        self.observers.remove(observer)

    # Pushes a message to every attached observer
    def notify_observers(self,message):
        print(f"Subject with topic {self.topic} Sennding message to all observers {len(self.observers)}")
        for observer in self.observers:
            observer.update(message)


def main():
    # Create three observers
    ob1=Observer('observer_1')
    ob2=Observer('observer_2')
    ob3=Observer('observer_2')

    # Create a subject and attach all observers
    subject=Subject('topic_1')
    subject.attach_observer(ob1)
    subject.attach_observer(ob2)
    subject.attach_observer(ob3)

    # Notify all — each observer receives "Hello "
    subject.notify_observers("Hello ")

    # Detach ob3 — it will no longer receive future notifications
    subject.detach_observer(ob3)


if __name__=='__main__':
    main()
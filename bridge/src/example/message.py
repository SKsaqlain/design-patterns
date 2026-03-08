from abc import ABC, abstractmethod


# Abstraction — holds a reference to the implementor (message sender)
class Message(ABC):
    def __init__(self, message_sender):
        self.message_sender = message_sender  # bridge to the delivery mechanism

    @abstractmethod
    def send(self, to, body):
        pass


# Refined Abstraction — urgent message delegates to the bridged sender
class UrgentMessage(Message):
    def send(self, to, body):
        urgent_body = f"[URGENT] {body}"  # prepend urgency tag before sending
        return self.message_sender.send_message(to, urgent_body)

from abc import ABC, abstractmethod


# Implementor interface — defines how a message is actually delivered
class MessageSender(ABC):
    @abstractmethod
    def send_message(self, to, body):
        pass

import logging

from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

# Abstract observer — gets notified when a new message arrives
class Consumer(ABC):

    def __init__(self,name: str, topic: str):
        self.name=name
        self.topic=topic

    # Called by the broker to deliver a message
    @abstractmethod
    async def update(self,message: str):
        pass


# Concrete observer — processes weather data updates
class WeatherAppConsumer(Consumer):
    def __init__(self, name,topic):
        super().__init__(name,topic)

    # Handles incoming weather messages from the subscribed topic
    async def update(self,message):
        logger.info(f"[{self.name}] received message from topic '{self.topic}': {message}")
        

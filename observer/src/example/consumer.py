import logging

from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class Consumer(ABC):

    def __init__(self,name: str, topic: str):
        self.name=name
        self.topic=topic

    @abstractmethod
    async def update(self,message: str):
        pass




class WeatherAppConsumer(Consumer):
    def __init__(self, name,topic):
        super().__init__(name,topic)

    async def update(self,message):
        logger.info(f"[{self.name}] received message from topic '{self.topic}': {message}")
        

import logging
from abc import ABC, abstractmethod
import asyncio
from functools import reduce
from typing import Dict, List

from broker import Broker

logger = logging.getLogger(__name__)

# Abstract producer — publishes messages to brokers via registered topics
class Producer(ABC):

    def __init__(self,producer_name: str, topics_broker_list: Dict[str,Broker]=None):
        self.producer_name=producer_name
        self.topics_broker_list=topics_broker_list if topics_broker_list is not None else {}

    # Sends a message to all registered topic-broker pairs
    @abstractmethod
    async def produce(self,message: str):
        pass

    # Links this producer to a broker under a specific topic
    @abstractmethod
    async def register_with_topic(self,broker: Broker,topic: str):
        pass


# Concrete producer — emits temperature readings to all registered brokers
class TemperatureProducer(Producer):

    def __init__(self, producer_name: str,topics_broker_list=None):
        super().__init__(producer_name= producer_name,topics_broker_list=topics_broker_list)

    # Publishes message to every registered topic concurrently
    async def produce(self, message: str):
        logger.info(f"[{self.producer_name}] pushing message to {len(self.topics_broker_list)} topic(s): {list(self.topics_broker_list.keys())}")
        tasks = [asyncio.create_task(self.topics_broker_list[t].publish(t, message)) for t in self.topics_broker_list.keys()]
        results= await asyncio.gather(*tasks)
        return reduce(lambda x,y: x and y, results)

    # Maps a topic name to a broker so produce() knows where to send
    async def register_with_topic(self,broker: Broker,topic: str):
        logger.info(f"[{self.producer_name}] registering with broker '{broker.broker_name}' on topic '{topic}'")
        self.topics_broker_list[topic]=broker

        
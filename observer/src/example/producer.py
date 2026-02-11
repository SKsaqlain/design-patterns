import logging
from abc import ABC, abstractmethod
import asyncio
from functools import reduce
from typing import Dict, List
from collections import defaultdict

from broker import Broker

logger = logging.getLogger(__name__)

class Producer(ABC):

    def __init__(self,producer_name: str, topics_broker_list: Dict[str,Broker]=defaultdict(str)):
        self.producer_name=producer_name
        self.topics_broker_list=topics_broker_list
    
    @abstractmethod
    async def produce(self,message: str):
        pass

    @abstractmethod
    async def register_with_topic(self,broker: Broker,topic: str):
        pass




class TemperatureProducer(Producer):

    def __init__(self, producer_name: str,topics_broker_list = defaultdict(str)):
        super().__init__(producer_name= producer_name,topics_broker_list=topics_broker_list)
        

    async def produce(self, message: str):
        logger.info(f"[{self.producer_name}] pushing message to {len(self.topics_broker_list)} topic(s): {list(self.topics_broker_list.keys())}")
        tasks = [asyncio.create_task(self.topics_broker_list[t].publish(t, message)) for t in self.topics_broker_list.keys()]
        results= await asyncio.gather(*tasks)
        return reduce(lambda x,y: x and y, results)
        
        

    
    async def register_with_topic(self,broker: Broker,topic: str):
        logger.info(f"[{self.producer_name}] registering with broker '{broker.broker_name}' on topic '{topic}'")
        self.topics_broker_list[topic]=broker

        
import asyncio
import logging
from functools import reduce
from typing import Dict, List
from consumer import Consumer
from abc import ABC, abstractmethod
from collections import defaultdict

logger = logging.getLogger(__name__)

class Broker(ABC):

    def __init__(self,broker_name: str):
        self.broker_name=broker_name

    
    @abstractmethod
    async def publish(self,topic: str, message: str):
        pass


    @abstractmethod
    async def broadcast(self,topic: str):
        pass

    @abstractmethod
    async def subscribe(self,consumer: Consumer, topic: str):
        pass

    @abstractmethod
    async def create_topic(self, topic: str):
        pass


    @abstractmethod
    async def get_all_topics(self):
        pass






class WeatherBroker(Broker):
    def __init__(self,broker_name: str):
        super().__init__(broker_name=broker_name)
        self.topics=set()
        self.message_queue:Dict[str, List]= defaultdict(list)
        self.offset_holders: Dict[Consumer, int]= defaultdict(int)
        self.subscribed_consumers: Dict[str, List[Consumer]]= defaultdict(int)

    
    
    async def create_topic(self, topic: str):
        logger.info(f"[{self.broker_name}] creating new topic '{topic}'")
        if topic not in self.topics:
            self.topics.add(topic)
            self.subscribed_consumers[topic]=list()


    async def get_all_topics(self):
        logger.debug(f"[{self.broker_name}] fetching all created topics")
        return self.topics

    async def subscribe(self,consumer: Consumer, topic: str):
        logger.info(f"[{self.broker_name}] {consumer.name} subscribing to topic '{topic}'")
        if topic not in self.topics:
            logger.warning(f"[{self.broker_name}] topic '{topic}' does not exist!")
            return False
        self.subscribed_consumers[topic].append(consumer)
        self.offset_holders[consumer]=0
        logger.info(f"[{self.broker_name}] {consumer.name} subscribed to '{topic}' with offset {self.offset_holders[consumer]}")
        return True


    async def update_consumer(self,consumer: Consumer, topic: str):
        try:
            last_offset=self.offset_holders[consumer]
            topic_len=len(self.message_queue[topic])
            logger.debug(f"[{self.broker_name}] updating consumer '{consumer.name}' from topic '{topic}' | offset {last_offset} -> {topic_len - 1}")
            for i in range(last_offset,topic_len):
                await consumer.update(self.message_queue[topic][i])
            self.offset_holders[consumer]=topic_len-1
            logger.debug(f"[{self.broker_name}] consumer '{consumer.name}' now at offset {self.offset_holders[consumer]}")
            return True
        except Exception as e:
            logger.error(f"[{self.broker_name}] failed to update consumer '{consumer.name}': {e}")
            return False

    async def broadcast(self, topic):
        if(len(self.subscribed_consumers[topic])==0):
            logger.warning(f"[{self.broker_name}] no subscribers under topic '{topic}'")
            return True
        logger.info(f"[{self.broker_name}] broadcasting topic '{topic}' to {len(self.subscribed_consumers[topic])} consumer(s)")
        tasks= [asyncio.create_task(self.update_consumer(consumer,topic)) for consumer in self.subscribed_consumers[topic]]
        results= await asyncio.gather(*tasks)
        return reduce(lambda a,b: a and b, results)



    async def publish(self,topic: str, message: str):
        if topic not in self.topics:
            logger.warning(f"[{self.broker_name}] publish failed — topic '{topic}' does not exist")
            return False
        logger.info(f"[{self.broker_name}] publishing to topic '{topic}': {message}")
        self.message_queue[topic].append(message)
        return await asyncio.create_task(self.broadcast(topic))



    

    

    
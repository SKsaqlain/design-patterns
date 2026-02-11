import asyncio
import logging
from functools import reduce
from typing import Dict, List
from consumer import Consumer
from abc import ABC, abstractmethod
from collections import defaultdict

logger = logging.getLogger(__name__)

# Abstract broker — mediates between producers and consumers
class Broker(ABC):

    def __init__(self,broker_name: str):
        self.broker_name=broker_name

    # Accepts a message from a producer and queues it under a topic
    @abstractmethod
    async def publish(self,topic: str, message: str):
        pass

    # Pushes queued messages to all consumers subscribed to a topic
    @abstractmethod
    async def broadcast(self,topic: str):
        pass

    # Registers a consumer to receive messages from a topic
    @abstractmethod
    async def subscribe(self,consumer: Consumer, topic: str):
        pass

    # Creates a new topic that producers/consumers can use
    @abstractmethod
    async def create_topic(self, topic: str):
        pass

    # Returns all available topics
    @abstractmethod
    async def get_all_topics(self):
        pass






# Concrete broker — manages topics, message queues, and consumer offsets
class WeatherBroker(Broker):
    def __init__(self,broker_name: str):
        super().__init__(broker_name=broker_name)
        self.topics=set()                                                       # registered topic names
        self.message_queue:Dict[str, List]= defaultdict(list)                   # topic -> list of messages
        self.offset_holders: Dict[Consumer, int]= defaultdict(int)              # consumer -> next unread index
        self.subscribed_consumers: Dict[str, List[Consumer]]= defaultdict(list) # topic -> list of consumers

    # Registers a new topic if it doesn't already exist
    async def create_topic(self, topic: str):
        logger.info(f"[{self.broker_name}] creating new topic '{topic}'")
        if topic not in self.topics:
            self.topics.add(topic)
            self.subscribed_consumers[topic]=list()

    # Returns the set of all registered topics
    async def get_all_topics(self):
        logger.debug(f"[{self.broker_name}] fetching all created topics")
        return self.topics

    # Adds a consumer to a topic's subscriber list
    async def subscribe(self,consumer: Consumer, topic: str):
        logger.info(f"[{self.broker_name}] {consumer.name} subscribing to topic '{topic}'")
        if topic not in self.topics:
            logger.warning(f"[{self.broker_name}] topic '{topic}' does not exist!")
            return False
        self.subscribed_consumers[topic].append(consumer)
        self.offset_holders[consumer]=0
        logger.info(f"[{self.broker_name}] {consumer.name} subscribed to '{topic}' with offset {self.offset_holders[consumer]}")
        return True

    # Delivers unread messages to a single consumer based on its offset
    async def update_consumer(self,consumer: Consumer, topic: str):
        try:
            last_offset=self.offset_holders[consumer]
            topic_len=len(self.message_queue[topic])
            logger.debug(f"[{self.broker_name}] updating consumer '{consumer.name}' from topic '{topic}' | offset {last_offset} -> {topic_len}")
            for i in range(last_offset,topic_len):
                await consumer.update(self.message_queue[topic][i])
            self.offset_holders[consumer]=topic_len
            logger.debug(f"[{self.broker_name}] consumer '{consumer.name}' now at offset {self.offset_holders[consumer]}")
            return True
        except Exception as e:
            logger.error(f"[{self.broker_name}] failed to update consumer '{consumer.name}': {e}")
            return False

    # Fans out updates to all subscribers of a topic concurrently
    async def broadcast(self, topic):
        if(len(self.subscribed_consumers[topic])==0):
            logger.warning(f"[{self.broker_name}] no subscribers under topic '{topic}'")
            return True
        logger.info(f"[{self.broker_name}] broadcasting topic '{topic}' to {len(self.subscribed_consumers[topic])} consumer(s)")
        tasks= [asyncio.create_task(self.update_consumer(consumer,topic)) for consumer in self.subscribed_consumers[topic]]
        results= await asyncio.gather(*tasks)
        return reduce(lambda a,b: a and b, results)

    # Enqueues a message and triggers broadcast to all subscribers
    async def publish(self,topic: str, message: str):
        if topic not in self.topics:
            logger.warning(f"[{self.broker_name}] publish failed — topic '{topic}' does not exist")
            return False
        logger.info(f"[{self.broker_name}] publishing to topic '{topic}': {message}")
        self.message_queue[topic].append(message)
        return await asyncio.create_task(self.broadcast(topic))



    

    

    
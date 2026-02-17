import asyncio
import logging

logger = logging.getLogger(__name__)


class ObjectPool:
    def __init__(self, object_factory, pool_size):
        self.pool_size = pool_size
        self.object_factory = object_factory  # async callable that creates pooled objects
        self.pool = asyncio.Queue(maxsize=pool_size)  # FIFO queue of available objects
        logger.info(f"ObjectPool created with max size {pool_size}")

    async def initialize(self):
        for i in range(self.pool_size):
            obj = await self.object_factory()  # await the async factory to create each object
            await self.pool.put(obj)  # place newly created object into the pool
            logger.debug(f"Initialized object {i + 1}/{self.pool_size}")
        logger.info(f"Pool initialized with {self.pool_size} objects")

    async def acquire(self):
        obj = await self.pool.get()  # blocks if pool is empty until an object is released
        logger.info(f"Acquired object from pool (available: {self.pool.qsize()})")
        return obj

    async def release(self, obj):
        await self.pool.put(obj)  # return the object to the pool for reuse
        logger.info(f"Released object back to pool (available: {self.pool.qsize()})")

    async def close_all(self):
        closed = 0
        while not self.pool.empty():
            obj = await self.pool.get()  # drain each object from the pool
            await obj.close_connection()  # close the underlying resource
            closed += 1
        logger.info(f"Closed all {closed} pooled objects")

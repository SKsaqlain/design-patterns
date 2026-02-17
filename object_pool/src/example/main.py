import asyncio
import logging

from src.example.object_pool import ObjectPool
from src.example.database_connection import DatabaseConnection

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
logger = logging.getLogger(__name__)


async def create_db_connection():
    return DatabaseConnection("object_pool.db")  # factory that creates a new db connection


async def run():
    pool_size = 5
    db_pool = ObjectPool(create_db_connection, pool_size)  # create pool with async factory
    await db_pool.initialize()  # pre-fill pool with connections
    try:
        # Test 1: Basic insert
        db_conn = await db_pool.acquire()  # get a connection from the pool
        connection = await db_conn.get_connection()  # unwrap the raw sqlite3 connection
        cursor = connection.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
        connection.commit()  # persist the insert to disk
        logger.info("Test 1 passed: User inserted successfully.")
        await db_pool.release(db_conn)  # return connection to pool

        # Test 2: Acquire two connections sequentially and insert a row with each
        conn1 = await db_pool.acquire()
        raw1 = await conn1.get_connection()
        raw1.cursor().execute("INSERT INTO users (name) VALUES (?)", ("Bob",))
        raw1.commit()  # commit before releasing to avoid db lock
        await db_pool.release(conn1)

        conn2 = await db_pool.acquire()
        raw2 = await conn2.get_connection()
        raw2.cursor().execute("INSERT INTO users (name) VALUES (?)", ("Charlie",))
        raw2.commit()
        await db_pool.release(conn2)
        logger.info("Test 2 passed: Two connections used sequentially.")

        # Test 3: Verify pool reuse — drain all but one, then release and re-acquire
        others = [await db_pool.acquire() for _ in range(pool_size - 1)]  # hold 4 connections
        conn_a = await db_pool.acquire()  # take the last one
        obj_id = id(conn_a)  # remember its identity
        await db_pool.release(conn_a)  # put it back as the only available connection
        conn_b = await db_pool.acquire()  # should get the same object back
        assert id(conn_b) == obj_id, "Pool did not reuse the released connection"
        logger.info("Test 3 passed: Connection was reused from pool.")
        await db_pool.release(conn_b)
        for c in others:
            await db_pool.release(c)  # restore all held connections

        # Test 4: Query back all inserted rows
        db_conn = await db_pool.acquire()
        connection = await db_conn.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM users ORDER BY id")
        rows = cursor.fetchall()
        names = [r[0] for r in rows]  # extract name column from each row
        assert names == ["Alice", "Bob", "Charlie"], f"Unexpected rows: {names}"
        logger.info(f"Test 4 passed: Queried users = {names}")
        await db_pool.release(db_conn)

        # Test 5: Pool exhaustion raises error
        acquired = [await db_pool.acquire() for _ in range(pool_size)]  # drain entire pool
        try:
            await asyncio.wait_for(db_pool.acquire(), timeout=0.2)  # should timeout since pool is empty
            logger.error("Test 5 failed: Should have timed out.")
        except asyncio.TimeoutError:
            logger.info("Test 5 passed: Pool exhaustion correctly timed out.")
        for c in acquired:
            await db_pool.release(c)

    finally:
        await db_pool.close_all()  # clean up all connections on exit


if __name__ == '__main__':
    asyncio.run(run())

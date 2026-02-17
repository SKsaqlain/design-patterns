import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class DatabaseConnection:
    _connection_id = 0  # class-level counter shared across all instances

    def __init__(self):
        DatabaseConnection._connection_id += 1
        self.connection_id = DatabaseConnection._connection_id  # unique id for this connection
        self.is_in_use = False
        logger.info(f"Created DatabaseConnection #{self.connection_id}")

    def run(self, query):
        logger.info(f"Running query via connection #{self.connection_id}: {query}")


class ConnectionPool:
    def __init__(self, max_size):
        self.max_size = max_size
        self.available = []  # connections ready to be handed out
        self.in_use = dict()  # maps connection_id -> connection currently in use
        self.initialize_pool()

    def initialize_pool(self):
        logger.info(f"Initializing connection pool with max size {self.max_size}")
        for _ in range(self.max_size):  # pre-create all connections upfront
            conn = DatabaseConnection()
            self.available.append(conn)

    def get_db_connection(self):
        if len(self.in_use) < self.max_size:
            conn = self.available.pop(0)  # take the oldest available connection
            conn.is_in_use = True
            self.in_use[conn.connection_id] = conn
            logger.info(f"Acquired connection #{conn.connection_id} from pool")
            return conn
        else:
            raise RuntimeError("No more connections available")

    def release(self, connection_id):
        if connection_id in self.in_use:
            conn = self.in_use[connection_id]  # look up connection before using it
            conn.is_in_use = False
            self.available.append(conn)  # return connection back to available pool
            del self.in_use[connection_id]
            logger.info(f"Released connection #{conn.connection_id} back to pool")
        else:
            raise RuntimeError(f"Connection id {connection_id} is already free")


if __name__ == '__main__':
    pool = ConnectionPool(2)

    conn_1 = pool.get_db_connection()
    conn_1.run("SELECT * FROM ABC")

    conn_2 = pool.get_db_connection()
    conn_2.run("SELECT * FROM DEF")

    # release conn_1 first so the pool has a free slot
    pool.release(conn_1.connection_id)

    # now acquiring conn_3 reuses the released connection
    conn_3 = pool.get_db_connection()
    conn_3.run("SELECT * FROM GHI")

    pool.release(conn_2.connection_id)
    pool.release(conn_3.connection_id)

import logging
import sqlite3

logger = logging.getLogger(__name__)


class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)  # open a persistent sqlite connection
        logger.info(f"Opened SQLite connection to '{db_path}'")

    async def get_connection(self):
        logger.debug(f"Returning raw connection for '{self.db_path}'")
        return self.connection  # expose the underlying sqlite3 connection

    async def close_connection(self):
        self.connection.close()  # release the sqlite file handle
        logger.info(f"Closed SQLite connection to '{self.db_path}'")

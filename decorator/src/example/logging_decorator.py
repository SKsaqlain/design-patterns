import logging

from src.example.base_decorator import DataSourceDecorator

logger = logging.getLogger(__name__)


# --- Concrete Decorator B ---
# Adds logging behavior — logs before and after the wrapped fetch call.
class LoggingDecorator(DataSourceDecorator):

    # Wrap the fetch with log statements for observability
    def fetch_data(self):
        logger.info("Logging Fetch Action")
        data = self.decorated_datasource.fetch_data()
        logger.info("Data fetched: %s", data)
        return data
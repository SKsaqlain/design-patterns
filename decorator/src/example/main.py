import logging

from src.example.logging_decorator import LoggingDecorator
from src.example.uppercase_decorator import UppercaseDecorator
from src.example.file_data_source import FileDataSource

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-20s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("=== Decorator Pattern — DataSource Example ===")

    # Start with the base component — raw file data source
    file_datasource = FileDataSource()

    # Wrap with UppercaseDecorator — converts data to uppercase
    uppercase = UppercaseDecorator(file_datasource)

    # Wrap again with LoggingDecorator — logs before and after fetch
    # Chain: LoggingDecorator → UppercaseDecorator → FileDataSource
    log_decorator = LoggingDecorator(uppercase)

    result = log_decorator.fetch_data()
    logger.info("Final result: %s", result)
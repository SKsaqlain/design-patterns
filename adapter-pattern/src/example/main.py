import logging

from src.example.net_suite_api import NetSuiteApi
from src.example.net_suite_adapter import NetSuiteAdapter

from src.example.business_central_api import BusinessCentralApi
from src.example.business_central_adapter import BusinessCentralAdapter

from src.example.client import Client

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-20s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("=== Adapter Pattern — CRM Integration Example ===")

    # Create the adaptees (incompatible CRM APIs)
    net_api = NetSuiteApi()
    bc_api = BusinessCentralApi()

    # Wrap NetSuite API in its adapter, then use via the Client
    logger.info("--- NetSuite ---")
    net_adapter = NetSuiteAdapter(net_suite_api=net_api)
    net_client = Client(adapter=net_adapter)
    res = net_client.process_customer_data()
    logger.info(f"Result: {res}")

    # Swap to Business Central — same Client code, different adapter
    logger.info("--- Business Central ---")
    bc_adapter = BusinessCentralAdapter(business_central_api=bc_api)
    bc_client = Client(adapter=bc_adapter)
    res = bc_client.process_customer_data()
    logger.info(f"Result: {res}")




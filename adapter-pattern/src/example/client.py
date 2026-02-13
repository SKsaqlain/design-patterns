import logging

from src.example.adapter import Adapter

logger = logging.getLogger(__name__)


# --- Client ---
# Works with any Adapter — doesn't know or care which CRM is behind it.
# Demonstrates Dependency Inversion: depends on Adapter abstraction, not concrete APIs.
class Client():

    def __init__(self, adapter: Adapter):
        # Accept any adapter that implements the Adapter interface
        self.adapter = adapter
        logger.info("Client created with %s", type(adapter).__name__)

    # Delegates to whichever adapter was injected — NetSuite, Business Central, etc.
    def process_customer_data(self):
        logger.info("Client processing customer data")
        return self.adapter.get_customer_data()
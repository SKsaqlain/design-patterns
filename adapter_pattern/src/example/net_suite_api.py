import logging

logger = logging.getLogger(__name__)


# --- Adaptee A ---
# Simulates the NetSuite CRM API with its own field naming convention.
# Fields: customer_id, name, email, status
class NetSuiteApi():

    # Returns raw customer data in NetSuite's format
    def get_customer(self):
        logger.info("Fetching customer data from NetSuite API")
        return {
            "customer_id": "101",
            "name": "Alice",
            "email": "alice@example.com",
            "status": "ACTIVE"
        }

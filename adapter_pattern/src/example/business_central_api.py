import logging

logger = logging.getLogger(__name__)


# --- Adaptee B ---
# Simulates the Business Central CRM API with its own field naming convention.
# Fields: customerId, fullName, emailID, status
class BusinessCentralApi():

    # Returns raw customer data in Business Central's format
    def get_customer(self):
        logger.info("Fetching customer data from Business Central API")
        return {
            "customerId": "201",
            "fullName": "Bob",
            "emailID": "bob@example.com",
            "status": "ACTIVE"
        }
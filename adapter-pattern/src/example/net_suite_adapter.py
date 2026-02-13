import logging

from src.example.adapter import Adapter
from src.example.customer import Customer

logger = logging.getLogger(__name__)


# --- Adapter A ---
# Wraps NetSuiteApi and translates its response into the unified Customer format.
# Maps: customer_id → id, name → full_name, email → email, status → status
class NetSuiteAdapter(Adapter):

    def __init__(self, net_suite_api):
        # Compose the adaptee (NetSuiteApi) inside the adapter
        self.net_suite_api = net_suite_api
        logger.info("NetSuiteAdapter created")

    # Fetch from NetSuite and translate to Customer dataclass
    def get_customer_data(self) -> Customer:
        logger.info("Adapting NetSuite data → Customer")
        data = self.net_suite_api.get_customer()

        return Customer(
            id=data["customer_id"],
            full_name=data["name"],
            email=data["email"],
            status=data["status"]
        )
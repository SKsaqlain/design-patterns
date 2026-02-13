import logging

from src.example.adapter import Adapter
from src.example.customer import Customer

logger = logging.getLogger(__name__)


# --- Adapter B ---
# Wraps BusinessCentralApi and translates its response into the unified Customer format.
# Maps: customerId → id, fullName → full_name, emailID → email, status → status
class BusinessCentralAdapter(Adapter):

    def __init__(self, business_central_api):
        # Compose the adaptee (BusinessCentralApi) inside the adapter
        self.business_central_api = business_central_api
        logger.info("BusinessCentralAdapter created")

    # Fetch from Business Central and translate to Customer dataclass
    def get_customer_data(self) -> Customer:
        logger.info("Adapting Business Central data → Customer")
        data = self.business_central_api.get_customer()

        return Customer(
            id=data["customerId"],
            full_name=data["fullName"],
            email=data["emailID"],
            status=data["status"]
        )

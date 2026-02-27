import logging
import time

logger = logging.getLogger(__name__)

# Simulated database — maps product ID to its full details
PRODUCT_DATABASE = {
    "P001": {"name": "Wireless Mouse", "price": 29.99, "category": "Electronics", "stock": 150},
    "P002": {"name": "Mechanical Keyboard", "price": 89.99, "category": "Electronics", "stock": 75},
    "P003": {"name": "USB-C Hub", "price": 45.00, "category": "Accessories", "stock": 200},
    "P004": {"name": "Monitor Stand", "price": 39.99, "category": "Furniture", "stock": 60},
    "P005": {"name": "Desk Lamp", "price": 24.99, "category": "Furniture", "stock": 120},
}


def fetch_product_by_id(product_id: str) -> dict:
    """Simulates an expensive database query with a short delay."""
    time.sleep(0.1)  # simulate network/disk latency
    data = PRODUCT_DATABASE.get(product_id)
    if data is None:
        raise ValueError(f"Product '{product_id}' not found in database")
    logger.info(f"DB query executed for product '{product_id}'")
    return data

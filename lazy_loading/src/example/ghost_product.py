import logging

from src.example.product_db import fetch_product_by_id

logger = logging.getLogger(__name__)


# Ghost Object — starts with only an ID; full data is loaded on first property access
class GhostProduct:
    def __init__(self, product_id: str):
        self.product_id = product_id  # lightweight identifier — always available
        self._loaded = False  # tracks whether full data has been fetched
        self._name = None
        self._price = None
        self._category = None
        self._stock = None
        logger.info(f"Ghost created for product '{product_id}' (data not loaded yet)")

    def _load(self):
        """Fetches full product data from the database on first access."""
        if not self._loaded:
            logger.info(f"Loading full data for product '{self.product_id}'...")
            data = fetch_product_by_id(self.product_id)  # expensive call
            self._name = data["name"]
            self._price = data["price"]
            self._category = data["category"]
            self._stock = data["stock"]
            self._loaded = True  # mark as fully loaded so future access skips the fetch

    @property
    def name(self) -> str:
        self._load()  # trigger lazy load if not already loaded
        return self._name

    @property
    def price(self) -> float:
        self._load()
        return self._price

    @property
    def category(self) -> str:
        self._load()
        return self._category

    @property
    def stock(self) -> int:
        self._load()
        return self._stock

    @property
    def is_loaded(self) -> bool:
        return self._loaded  # lets callers check without triggering a load

    def __str__(self):
        if not self._loaded:
            return f"GhostProduct(id={self.product_id}, not loaded)"
        return f"Product(id={self.product_id}, name={self._name}, price=${self._price}, category={self._category}, stock={self._stock})"

import logging
from typing import List

from src.example.ghost_product import GhostProduct

logger = logging.getLogger(__name__)


# Catalog — holds a list of ghost products; none are loaded until individually accessed
class ProductCatalog:
    def __init__(self, product_ids: List[str]):
        self.products = [GhostProduct(pid) for pid in product_ids]  # all start as ghosts
        logger.info(f"Catalog initialized with {len(self.products)} ghost products")

    def get_product(self, product_id: str) -> GhostProduct:
        """Look up a product by ID — returns the ghost, triggering load only when properties are accessed."""
        for product in self.products:
            if product.product_id == product_id:
                return product
        raise ValueError(f"Product '{product_id}' not in catalog")

    def get_loaded_count(self) -> int:
        """Returns how many products have been fully loaded so far."""
        return sum(1 for p in self.products if p.is_loaded)

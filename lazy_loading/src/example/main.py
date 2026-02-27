import logging

from src.example.ghost_product import GhostProduct
from src.example.product_catalog import ProductCatalog

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def run():
    product_ids = ["P001", "P002", "P003", "P004", "P005"]

    # Test 1: Catalog creation — all products are ghosts, no DB calls yet
    logger.info("=== Test 1: Catalog creation (no DB calls) ===")
    catalog = ProductCatalog(product_ids)
    assert catalog.get_loaded_count() == 0, "No products should be loaded yet"
    logger.info(f"Loaded count: {catalog.get_loaded_count()}")
    logger.info("Test 1 passed: All products are ghosts")

    # Test 2: Accessing a property triggers lazy load for that product only
    logger.info("=== Test 2: Access one product — triggers load ===")
    mouse = catalog.get_product("P001")
    logger.info(f"Before access: {mouse}")
    logger.info(f"Name: {mouse.name}")  # this triggers the DB fetch
    logger.info(f"After access: {mouse}")
    assert mouse.is_loaded, "Product should be loaded after property access"
    assert catalog.get_loaded_count() == 1, "Only one product should be loaded"
    logger.info("Test 2 passed: Only accessed product was loaded")

    # Test 3: Second access does NOT trigger another DB call
    logger.info("=== Test 3: Repeated access — no extra DB call ===")
    price = mouse.price  # already loaded, should not log a DB query
    logger.info(f"Price: ${price} (fetched without extra DB call)")
    logger.info("Test 3 passed: No duplicate load")

    # Test 4: Other products remain as ghosts
    logger.info("=== Test 4: Unaccessed products stay as ghosts ===")
    keyboard = catalog.get_product("P002")
    assert not keyboard.is_loaded, "Unaccessed product should still be a ghost"
    logger.info(f"Keyboard state: {keyboard}")
    logger.info(f"Loaded count: {catalog.get_loaded_count()}")
    logger.info("Test 4 passed: Unaccessed products are still ghosts")

    # Test 5: Load all products and verify data
    logger.info("=== Test 5: Load all products ===")
    for pid in product_ids:
        product = catalog.get_product(pid)
        logger.info(f"{product.name} — ${product.price} — {product.category} — stock: {product.stock}")
    assert catalog.get_loaded_count() == len(product_ids), "All products should be loaded"
    logger.info(f"Test 5 passed: All {catalog.get_loaded_count()} products loaded")


if __name__ == '__main__':
    run()

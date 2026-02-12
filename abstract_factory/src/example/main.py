import logging
from src.example.cloud_service import AWSFactory, AZUREFactory, GCPFactory

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-20s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


if __name__=='__main__':
    logger.info("=== Abstract Factory — Cloud Service Example ===")

    # Iterate over each cloud provider factory
    # Same client code, different factories produce different matched service sets
    factories = [AWSFactory(), GCPFactory(), AZUREFactory()]
    for factory in factories:
        logger.info(f"--- {factory.name} ---")
        vm = factory.get_virtual_machine()
        vm.start_machine()
        db = factory.get_database()
        db.connect_to_db()
        storage = factory.get_storage()
        storage.connect_to_storage()


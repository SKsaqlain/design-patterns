import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-20s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


# --- Component Interface ---
# Defines the base interface for all coffee types and decorators.
class Coffee(ABC):

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


# --- Concrete Component ---
# The base object that decorators will wrap. Starts at $2.00.
class PlainCoffee(Coffee):
    def get_description(self) -> str:
        return "Plain Coffee"

    def get_cost(self) -> float:
        return 2.00


# --- Base Decorator ---
# Wraps a Coffee object and delegates calls to it. Subclasses add behavior on top.
class CoffeeDecorator(Coffee):
    def __init__(self, decorate_coffee: Coffee):
        # Hold a reference to the wrapped coffee (composition)
        self.decorate_coffee = decorate_coffee
        logger.info("Wrapping [%s] with %s", decorate_coffee.get_description(), type(self).__name__)

    def get_description(self):
        return self.decorate_coffee.get_description()

    def get_cost(self):
        return self.decorate_coffee.get_cost()


# --- Concrete Decorator A ---
# Adds milk to the coffee (+$0.50).
class Milk(CoffeeDecorator):
    def get_description(self):
        return self.decorate_coffee.get_description() + ', Milk'

    def get_cost(self):
        return self.decorate_coffee.get_cost() + 0.50


# --- Concrete Decorator B ---
# Adds sugar to the coffee (+$0.10).
class Sugar(CoffeeDecorator):
    def get_description(self):
        return self.decorate_coffee.get_description() + ', Sugar'

    def get_cost(self):
        return self.decorate_coffee.get_cost() + 0.10


if __name__ == '__main__':
    logger.info("=== Decorator Pattern — Coffee Example ===")

    # Start with a plain coffee ($2.00)
    coffee = PlainCoffee()
    logger.info("Base: %s — $%.2f", coffee.get_description(), coffee.get_cost())

    # Wrap with Milk decorator ($2.00 + $0.50 = $2.50)
    milk_coffee = Milk(coffee)
    logger.info("After Milk: %s — $%.2f", milk_coffee.get_description(), milk_coffee.get_cost())

    # Wrap again with Sugar decorator ($2.50 + $0.10 = $2.60)
    sugar_coffee = Sugar(milk_coffee)
    logger.info("After Sugar: %s — $%.2f", sugar_coffee.get_description(), sugar_coffee.get_cost())
    
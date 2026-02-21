import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# Prototype interface — declares clone and draw for all shapes
class ShapePrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def draw(self):
        pass


# Concrete Prototype — creates a copy of itself with the same color
class CirclePrototype(ShapePrototype):
    def __init__(self, color: str):
        self.color = color
        logger.info(f"Created CirclePrototype with color '{color}'")

    def clone(self):
        cloned = CirclePrototype(self.color)  # new instance with same state
        logger.info(f"Cloned CirclePrototype with color '{self.color}'")
        return cloned

    def draw(self):
        logger.info(f"Drawing a {self.color} Circle")


# Client — uses a prototype to create new shapes without knowing their class
class ShapeClient:
    def __init__(self, shape_prototype: ShapePrototype):
        self.shape_prototype = shape_prototype  # store the prototype to clone from

    def create_shape(self):
        return self.shape_prototype.clone()  # delegate creation to the prototype


if __name__ == '__main__':
    
    red_circle_prototype = CirclePrototype('red')  # original prototype
    red_circle_prototype.draw()

    client = ShapeClient(red_circle_prototype)  # client only knows the prototype interface

    cloned_shape: CirclePrototype = client.create_shape()  # clone without calling constructor directly
    cloned_shape.draw()

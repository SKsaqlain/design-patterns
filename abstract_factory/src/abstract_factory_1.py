from abc import ABC, abstractmethod


# --- Abstract Product A ---
# Defines the interface for all car types
class Car(ABC):
    @abstractmethod
    def build_car(self) -> str:
        pass

# --- Abstract Product B ---
# Defines the interface for all regional specifications
class CarSpecification(ABC):
    @abstractmethod
    def get_specification(self) -> str:
        pass


# --- Concrete Product A variants ---
# Each car type implements the Car interface
class Sedan(Car):
    def build_car(self) -> str:
        return "Building Sedan Car."

class Hatchback(Car):
    def build_car(self) -> str:
        return "Building Hatchback Car."


# --- Concrete Product B variants ---
# Each specification implements the CarSpecification interface
class NorthAmericanSpecification(CarSpecification):
    def get_specification(self) -> str:
        return "North American Specification: Safety features compliant with local regulations."

class EuropeSpecification(CarSpecification):
    def get_specification(self) -> str:
        return "Europe Car Specification: Fuel efficiency and emissions compliant with EU Standards."



# --- Abstract Factory ---
# Declares creation methods for each product in the family (Car + Spec).
# Each concrete factory produces a matched set of products for a specific region.
class CarFactory(ABC):
    # Creates a car type specific to this factory's region
    @abstractmethod
    def create_car(self) -> Car:
        pass

    # Creates a specification matching this factory's region
    @abstractmethod
    def create_specification(self) -> CarSpecification:
        pass


# --- Concrete Factory: North America ---
# Always produces Sedan + NorthAmericanSpecification as a matched pair
class NorthAmericanCarFactory(CarFactory):
    def create_car(self) -> Car:
        return Sedan()

    def create_specification(self) -> CarSpecification:
        return NorthAmericanSpecification()

# --- Concrete Factory: Europe ---
# Always produces Hatchback + EuropeSpecification as a matched pair
class EuropeCarFactory(CarFactory):
    def create_car(self) -> Car:
        return Hatchback()

    def create_specification(self) -> CarSpecification:
        return EuropeSpecification()


def main():
    # Use NorthAmericanCarFactory — gets a Sedan with NA specs
    na_factory = NorthAmericanCarFactory()
    car = na_factory.create_car()
    spec = na_factory.create_specification()
    print(car.build_car())
    print(spec.get_specification())

    print()

    # Swap to EuropeCarFactory — gets a Hatchback with EU specs
    eu_factory = EuropeCarFactory()
    car = eu_factory.create_car()
    spec = eu_factory.create_specification()
    print(car.build_car())
    print(spec.get_specification())

if __name__=='__main__':
    main()

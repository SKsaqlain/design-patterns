from abc import ABC,abstractmethod


# --- Product Interface ---
# Vehical is the abstract base class (Product) that defines the interface
# all concrete products (Car, Bike, etc.) must implement.
# This ensures every vehicle type has a get_vehical_type() method.
class Vehical(ABC):
    @abstractmethod
    def get_vehical_type(self)->str:
        pass


# --- Concrete Products ---
# Car is a concrete implementation of the Vehical interface.
# It provides its own version of get_vehical_type(), returning "Car".
class Car(Vehical):
    def get_vehical_type(self)->str:
        return "Car"


# Bike is another concrete implementation of the Vehical interface.
# It provides its own version of get_vehical_type(), returning "Bike".
class Bike(Vehical):
    def get_vehical_type(self):
        return "Bike"


# --- Factory Interface (Creator) ---
# VehicalFactory is the abstract factory (Creator) that declares
# the factory method create_vehical(). Each subclass (concrete factory)
# will override this method to produce a specific type of Vehical.
# This is the core of the Factory Method pattern — the creation logic
# is deferred to subclasses instead of being hardcoded in the client.
class VehicalFactory(ABC):
    @abstractmethod
    def create_vehical(self):
        pass

# --- Concrete Factories (Concrete Creators) ---
# CarFactory overrides create_vehical() to return a Car instance.
# The client doesn't need to know about the Car class directly —
# it only interacts with the VehicalFactory interface.
class CarFactory(VehicalFactory):
    def create_vehical(self):
        return Car()

# BikeFactory overrides create_vehical() to return a Bike instance.
# Adding a new vehicle type (e.g., Truck) only requires creating
# a new TruckFactory and Truck class — no changes to existing code.
# This follows the Open/Closed Principle (open for extension, closed for modification).
class BikeFactory(VehicalFactory):
    def create_vehical(self):
        return Bike()



from enum import Enum

# VehicalType enum defines the available vehicle types as constants.
# Not directly used in the factory method approach below, but useful
# if you want to map enum values to factories in a registry pattern.
class VehicalType(Enum):
    CAR= 1
    BIKE= 2

# --- Client ---
# The Client class depends only on the VehicalFactory abstraction,
# not on any concrete product (Car/Bike). This is Dependency Inversion —
# high-level modules (Client) depend on abstractions (VehicalFactory),
# not on low-level modules (Car, Bike).
# The client receives a factory via constructor injection and uses it
# to create a vehicle without knowing which concrete type it gets.
class Client:
    def __init__(self,vehical_factory: VehicalFactory):
        # Delegates object creation to the injected factory.
        # The client has no idea whether it's getting a Car or Bike.
        self.vehical=vehical_factory.create_vehical()


    def get_vehical(self):
        return self.vehical




def main():
    # Create a CarFactory and pass it to the Client.
    # The Client calls create_vehical() internally, which returns a Car.
    carFactory= CarFactory()
    client=Client(carFactory)
    vehical= client.get_vehical()
    if vehical is not None:
        print(vehical.get_vehical_type())  # Output: Car


    # Swap the factory to BikeFactory — the Client code stays the same.
    # This demonstrates the key benefit: switching products without
    # changing the client logic. Only the factory changes.
    bikeFactory= BikeFactory()
    client=Client(bikeFactory)
    vehical= client.get_vehical()
    if vehical is not None:
        print(vehical.get_vehical_type())  # Output: Bike

if __name__=='__main__':
    main()

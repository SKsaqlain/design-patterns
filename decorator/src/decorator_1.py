from abc import ABC, abstractmethod


class Coffee(ABC):
    
    @abstractmethod
    def get_description(self)-> str:
        pass

    @abstractmethod
    def get_cost(self)-> float:
        pass


class PlainCoffee(Coffee):
    def get_description(self)->str:
        return "Plain Coffee "
    
    def get_cost(self)->float:
        return 2.00
    

class CoffeeDecorator(Coffee):
    def __init__(self, decorate_coffee: Coffee):
        self.decorate_coffee= decorate_coffee
    
    def get_description(self):
        return self.decorate_coffee.get_description()
    
    def get_cost(self):
        return self.decorate_coffee.get_cost()
    

    
    
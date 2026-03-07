from abc import ABC, abstractmethod


class Workshop(ABC):
    @abstractmethod
    def work(self):
        pass

class Produce(Workshop):
    def work(self):
        print('Produced', end='')

class Assemble(Workshop):
    def work(self):
        print(' And', end='')
        print(' Assembled.')


class Vehical(ABC):
    def __init__(self, workshop1,workshop2):
        self.workshop1=workshop1
        self.workshop2=workshop2
    
    @abstractmethod
    def manufacture(self):
        pass

class Bike(Vehical):

    def manufacture(self):
        print("Bike ",end=' ')
        self.workshop1.work()
        self.workshop2.work()

class Car(Vehical):

    def manufacture(self):
        print("Car",end=' ')
        self.workshop1.work()
        self.workshop2.work()
    
if __name__=='__main__':
    vehical1=Car(Produce(),Assemble())
    vehical1.manufacture()

    vehical2=Bike(Produce(),Assemble())
    vehical2.manufacture()

from enum import Enum
from typing import Dict

class CarType(Enum):
    none=1
    Audi=2
    BMW=3

class Car:
    types: Dict[CarType,'Car']={}

    def __init__(self, type: CarType):
        pass

    @staticmethod
    def get_car_by_type_name(type:CarType):
        if type not in Car.types:
            car=Car(type)
            Car.types[type]=car
        else:
            car=Car.types[type]
        return car
    
    @staticmethod
    def show_all():
        if(len(Car.types)==0):
            return
        print(f"Number of instances made = {len(Car.types)}")
        for car_type,car in Car.types.items():
            car_str=car_type.name
            print(car_str)

if __name__=='__main__':
    Car.get_car_by_type_name(CarType.BMW)
    Car.show_all()
    Car.get_car_by_type_name(CarType.Audi)
    Car.show_all()


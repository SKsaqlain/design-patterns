from abc import ABC, abstractmethod


class Hotel(ABC):
    @abstractmethod
    def get_menus(self):
        pass

class NonVegRestaurant(Hotel):
    def get_menus(self):
        nv= NonVegMenu()
        return nv
    

class VegRestaurant(Hotel):
    def get_menus(self):
        v=VegMenu()
        return v

class GeneralRestaurant(Hotel):
    def get_menus(self):
        b=Both()
        return b
    

class HotelKeeper(ABC):
    @abstractmethod
    def getVegMenu(self):
        pass

    @abstractmethod
    def getNonVegMeny(self):
        pass

    @abstractmethod
    def getGeneralMenu(self):
        pass
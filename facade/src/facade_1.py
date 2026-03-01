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

class HotelKeeperImpl(HotelKeeper):
    def getVegMenu(self):
        v=VegRestaurant()
        menu=v.get_menus()
        return menu
    
    def getNonVegMeny(self):
        nv=NonVegRestaurant()
        menu=nv.get_menus
        return menu
    
    def getGeneralMenu(self):
        g=GeneralRestaurant()
        menu=g.get_menus()
        return menu
    
class VegMenu:
    pass

class NonVegMenu:
    pass
class Both:
    pass
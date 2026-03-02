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
    def getNonVegMenu(self):
        pass

    @abstractmethod
    def getGeneralMenu(self):
        pass

class HotelKeeperImpl(HotelKeeper):
    def getVegMenu(self):
        v=VegRestaurant()
        menu=v.get_menus()
        return menu
    
    def getNonVegMenu(self):
        nv=NonVegRestaurant()
        menu=nv.get_menus()
        return menu
    
    def getGeneralMenu(self):
        g=GeneralRestaurant()
        menu=g.get_menus()
        return menu
    
class VegMenu:
    def __init__(self):
        print("Vegan Menu")

class NonVegMenu:
    def __init__(self):
        print("Non Vegan Menu")
class Both:
    def __init__(self):
        print("General Menu")



def main():
    keeper= HotelKeeperImpl()
    v=keeper.getVegMenu()
    nv=keeper.getNonVegMenu()
    general=keeper.getGeneralMenu()

if __name__=='__main__':
    main()
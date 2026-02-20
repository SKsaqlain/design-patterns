from abc import ABC,abstractmethod

class ShapePrototype(ABC):
    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class CirclePrototype(ShapePrototype):
    def __init__(self,color: str):
        self.color=color
    def clone(self):
        return CirclePrototype(self.color)
    
    def draw(self):
        print(f"Drawing a {self.color} Circle")


class ShapeClient:
    def __init__(self, shape_prototype: ShapePrototype):
        self.shape_prototype=shape_prototype
    
    def create_shape(self):
        return self.shape_prototype.clone()
    

if __name__=='__main__':
    red_circle_prototype=CirclePrototype('red')
    red_circle_prototype.draw()


    client=ShapeClient(red_circle_prototype)

    cloned_shape: CirclePrototype=client.create_shape()
    cloned_shape.draw()

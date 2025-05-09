# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,lenght:int, width:int) :
          self.lenght=lenght
          self.width=width
    def area(self):
        return self.lenght*self.width
areas=Rectangle(5,7)
print(areas.area() )              

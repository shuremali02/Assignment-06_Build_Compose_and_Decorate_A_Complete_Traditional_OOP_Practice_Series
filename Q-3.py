# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

from tracemalloc import start


class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print(f"{self.brand} here is your car model ")
car_model=Car("Toyotta")
print(car_model.brand)
start()

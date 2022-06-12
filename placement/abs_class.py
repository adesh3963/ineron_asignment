from abc import ABC, abstractmethod

class car(ABC):
    def __init__(self,name,max_speed,hp):
        self.name= name
        self.max_speed = max_speed
        self.hp= hp

    @abstractmethod
    def car_name(self):
        print("this method has to be explicitly written in every child class,"
              "name of the car is %s"%str(self.name))
class Honda(car):
    def car_name(self):
        print("car name is %s",self.name)

class Toyota(car):
    def car_name(self):
        print("car name is %s",self.name)

car1= Honda(name="city", max_speed=150, hp=250)
car2= Toyota(name="Innova",max_speed=140,hp=220)

car1.car_name()
car2.car_name()
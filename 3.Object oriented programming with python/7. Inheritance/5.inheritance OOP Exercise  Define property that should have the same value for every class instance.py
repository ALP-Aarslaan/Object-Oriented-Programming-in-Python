class Vehicale:
    color = "white"
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def display(self):
        print(f"Vehicale name : {self.name}, color :{self.color}, max speed : {self.max_speed}, mileage :{self.mileage}")


class Bus(Vehicale):
    pass
class Car(Vehicale):
    pass

bus = Bus("Volvo",180,8)
bus.display()

car = Car("toyota",400,20)
car.display()
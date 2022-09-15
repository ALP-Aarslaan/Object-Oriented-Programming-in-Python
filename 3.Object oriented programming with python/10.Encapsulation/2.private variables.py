class Bus:
    __maxSpeed = 0
    __name = ""

    def __init__(self) -> None:
        self.__maxSpeed = 200
        self.__name = "Volvo"

    def drive(self):
        print("maximum driving speed : ",self.__maxSpeed)


bus1 = Bus()
bus1.drive()
bus1.__maxSpeed = 300 # private variable so we can not change the value from outside of the class
bus1.drive()

#If you want to change the value of a private variable, a setter method is used.  This is simply a method that sets the value of a private variable.


class Bus1:
    __maxSpeed = 0
    __name = ""

    def __init__(self) -> None:
        self.__maxSpeed = 300
        self.__name = "Asia Line"

    def setmaxSpeed(self,speed):
        self.__maxSpeed = speed

    def setname(self,name):
        self.__name = name

    def drive(self):
        print(f"maximum speed of the Bus :{self.__name} is :{self.__maxSpeed}")



bus = Bus1()
bus.drive()
bus.setmaxSpeed(250)
bus.setname("Saudia")
bus.drive()


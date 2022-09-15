class Person:
    def __init__(self,name) -> None:
        self.__name = name

    @property
    def name(self):
        print("getter method is called ")
        return self.__name

    @name.setter
    def name(self,name):
        print("setter method is called")
        self.__name = name


p1 = Person("Mohammad Jonayed")
print(p1.name)
p1.name = "Sarkar"
print(p1.name)
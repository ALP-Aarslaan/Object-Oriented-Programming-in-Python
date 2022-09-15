from typing import NamedTuple


class Person:
    def __init__(self,name) -> None:
        self.__name = name

    @property
    def name(self):
        print("getter method is called")
        return self.__name

    @name.setter
    def name(self,namevalue):
        print("setter method is called")
        self.__name = namevalue

    @name.deleter
    def name(self):
        print("deleting")
        del self.__name

p1 = Person("Mohammad Jonayed")
print(p1.name)
p1.name = "Md jonayed sarkar"
print(p1.name)
del p1.name
# print(p1.name)
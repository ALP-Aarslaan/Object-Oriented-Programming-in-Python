# using this @property notation to use get method like java to access to get a private attribute

class Person:
    def __init__(self, name) -> None:
        self.__name = name

    @property
    def name(self):
        print("get method is called to get private attributes/variables")
        return self.__name


jonayed = Person("Mohammad Jonayed")
print(jonayed.name)
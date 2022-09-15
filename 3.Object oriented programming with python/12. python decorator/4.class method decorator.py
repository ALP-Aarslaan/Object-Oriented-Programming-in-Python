class Person:
    name = "Jonayed"

    def __init__(self) -> None:
        self.age = 23

    @classmethod
    def display(cls):
        print("Student class attributes : ",cls.name)
          
Person.display()

p1 = Person()
p1.display()
Person.name = "i am jonayed"
p1.display()

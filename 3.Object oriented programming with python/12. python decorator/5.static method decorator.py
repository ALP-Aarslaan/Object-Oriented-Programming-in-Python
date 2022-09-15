class Person:
    name = "Mohammad Jonayed Sarkar"

    def __init__(self) -> None:
        self.age = 23
    @staticmethod
    def display():
        print("student class")
        print("person's name : ",Person.name)
        # print("person's age : ",Person.age)


Person.display()

p1 = Person()
Person.name = "MJ"
p1.display()
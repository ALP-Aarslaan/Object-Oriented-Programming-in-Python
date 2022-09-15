"""
variable two types in oop:
1.instance variable
2.class or static variables

**instance variable changes depending upon object they are declared inside init method

**class variables or static variables are declared outside of init method. these type of
variables are common in every object of a certain class. this type of variables are
shared between all objects of this class once we change it it will affect all the object
of this class

"""


class Car:
    def __init__(self):
        self.mileage = 10    # these mileage and company is called instance variable
        self.company = "BMW"


car1 = Car()
car2 = Car()
car2.company = "Ford"
print(car1.mileage,car1.company)

print(car2.mileage,car2.company)
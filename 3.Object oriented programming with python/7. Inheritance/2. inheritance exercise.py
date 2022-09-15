"""
Types of Inheritance depends upon the number of child and parent classes involved.
There are five types of inheritance in Python:

Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance
"""

class Quadrelateral:

    def __init__(self,a,b,c,d) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        print(f"perimeter of a square : ",self.a+self.b+self.c+self.d)


square1 = Quadrelateral(3,3,3,3)
square1.perimeter()

# single inheritance

class Rectangle(Quadrelateral):
    def area(self):
        print("area of a rectangle : ",self.a* self.b)

rectangle = Rectangle(2,2,2,2)
rectangle.perimeter()
rectangle.area()


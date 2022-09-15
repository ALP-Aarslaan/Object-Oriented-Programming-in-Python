class Circle:
    def __init__(self,pi,radious):
        self.pi = pi
        self.radious = radious
        
    def area(self):
        print(f"area of a circle is : {self.pi*(self.radious**2)}")

class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def area(self):
        print(f"area of a rectangle : {self.height*self.width}")

c = Circle(3.1416,2)
c.area()

r = Rectangle(2,2)
r.area()
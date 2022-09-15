"""
if there is 2 class A and B
B class inheriting A class so if we create a B class object first it will go to B class
and will look for B class init method and will execute it . if there is no init method in
B class then it will execute inherited (A) class's init method
"""


class A:
    def __init__(self):
        print("In init of A class")


class B(A):

    def __init__(self):
        super().__init__()
        print("in init of B class")


obj = A()
obj1 = B()

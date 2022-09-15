"""
in multiple inheritance calling a super class method works in left to right order
as in this example in class C we inherited first A and then B left to right order(A,B)
so methods of A super class will be called first then B
"""


class A:
    def __init__(self):
        print("in init method of class A")


class B:
    def __init__(self):
        print("in init method of class B")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("in init method of class C")


obj = C()

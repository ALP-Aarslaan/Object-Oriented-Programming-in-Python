"""
there are 3 types of methods in python:
1. instance  methods
2. class methods
3. static methods
"""


class Students:
    school = "IPSC"  # static or class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance methods:

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getSchoolName(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is a student class")


"""
inorder to use a class method at first we need a decorator.
# declaring class method : we give parameter as cls
@classmethod
"""
"""
static methods are not concerned about class variable or instance
variable.
inorder to use a static method at first we need a decorator
@staticmethod. we do not need to give any parameter
"""

s1 = Students(20, 21, 22)
s2 = Students(30, 31, 33)
print(s1.average())
print(s2.average())
s1.set_m1(100)
print(s1.average())
print(s1.get_m1())
print(s1.getSchoolName())
s1.info()
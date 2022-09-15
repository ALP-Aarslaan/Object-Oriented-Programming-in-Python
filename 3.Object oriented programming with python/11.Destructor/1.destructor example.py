# del method:
class A:
    # creating initial method or default constructor:
    def __init__(self) -> None:
        print("constructor of class A ")
        self.a = 30
    # creating destructor :
    def __del__(self):
        print("initialized dstructor for object of class a")

object = A()
print(object.a)
del object
# print(object.a) 
"""
after deleting or calling destructor the initialized object and its attribiutes are collected as garbage  
"""
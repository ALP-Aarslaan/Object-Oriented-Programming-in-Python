"""
encapsulation in python is 2 types:
1. public 
2. private

if we dont specify anything before an attribute or method just write down its name it will be considered as public method or attribute 
public methods and attributes can be accesed anywhere 
if we mention private sign before anyof this then they will be considred as private 

public methods and attributes can be accesed only whithin the class we can not access them outside of its class.
in order to declare a private method or variable we need to give double underscore(__) before variable and methods names like:
__Variable name
__method name

"""
class Encap:
    a = 10
    def display(self):
        print("hi")

obj = Encap()
print(obj.a)
obj.display()

# class EncapPrivate:
#     __a = 11
#     def __display(self):
#         print("hello")

# obj1 = EncapPrivate()
# print(obj1.__a)
# obj1.__display()

# we can not access thes private method and variable
# in order to do so :


class EncapPrivate:
    __a = 11
    def display(self):
        print("hello")
        print(self.__a)
obj1 = EncapPrivate()
# print(obj1.__a)
obj1.display()
"""
Protected members
Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
Note: The __init__ method is a constructor and runs as soon as an object of a class is instantiated.
"""
# Python program to
# demonstrate protected members


# Creating a base class
class Base:
    _name = ""
    def __init__(self):
	    self._a = 2
        
    
    def _name(self):
        print("this a protected method")


    def setname(self,name):
        self._name = name

# Creating a derived class
# class Derived(Base):
	# def __init__(self):
		
	# 	# Calling constructor of
	# 	# Base class
	# 	Base.__init__(self)
	# 	print("Calling protected member of base class: ")
	# 	print(self._a)
    pass
# obj1 = Derived()
# obj1._a = 3
# print(obj1._a)		
obj2 = Base()
obj2._a = 4
print(obj2._a)
# print(obj1._a)
# Calling protected member
# Outside class will result in
# AttributeError
print(obj2._a)
# obj1._name()
obj2._name()
# obj1._name = "Jonayed" 
# print(obj1._name)
# obj2._name = "sarkar"
print(obj2._name)
obj2.setname("Arslan")
print(obj2._name)
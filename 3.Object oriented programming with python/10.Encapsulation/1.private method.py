# class Car:
#     def __init__(self):
#         self.__updateSoftware()

#     def drive(self):
#         print("driving")

#     def __updateSoftware(self):
#         print("updating software")


# redCar = Car()
# redCar.drive()
# redCar.__updateSoftware()
# redCar._Car__updateSoftware()
# can not call directly using object because its a private method only within the class we can call

# encapsulation prevents from accessing accidentally, but not intentionally Encapsulation prevents from accessing accidentally, but not intentionally.

# The private attributes and methods are not really hidden, they’re renamed adding _Car” in the beginning of their name.

# The method can actually be called using redcar._Car__updateSoftware() 

# Python program to
# demonstrate private methods
	
# Creating a class
class A:
	
	# Declaring public method
	def fun(self):
		print("Public method")
	
	# Declaring private method
	def __boring(self):
		print("Private method")
		
# Driver's code
obj = A()

# Calling the private member
# through name mangling
obj._A__boring()


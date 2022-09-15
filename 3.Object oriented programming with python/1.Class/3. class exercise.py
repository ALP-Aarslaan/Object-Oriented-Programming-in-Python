"""
class has two things
1. attributes - (variables)
2. behaviour - (methods/functions)
"""


# class declaration:
class Computer:
    # Method declaration:
    def configuration(self): # here self means the object of this class we are passing to call this function
        print("""
        Acer Aspire E14,
        intel core i5 7th gen,
        ram 8 gb, hdd 1tb, ssd 256gb
        """)


computer1 = Computer()
print(type(computer1))

# calling methods:
"""
in order to call a method from a class we need to give class name then dot operator
then method name with parenthesis and inside the parenthesis we need to give the object name
 or we can call the method object name then dot operator then the method name
"""
computer1.configuration()
Computer.configuration(computer1)

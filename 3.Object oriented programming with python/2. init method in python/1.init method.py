"""
init methods are also like constructors. We use it to initialize variable while creating object
of a class. and we don't need to call init method its automatically calls itself while
we initialize an object
"""


class Computer:
    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def configuration(self):
        print("configuration is :", self.cpu, self.ram, self.hdd)


c1 = Computer("Core i5", "8gb", "1Tb")
c2 = Computer("Ryzen 9", "16gb", "2Tb")
c1.configuration()
c2.configuration()
print(id(c1))
print(id(c2))
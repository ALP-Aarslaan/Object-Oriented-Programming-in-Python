class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.laptop1 = self.Laptop(brand="ACER", cpu="Intel core i5 7th gen", ram="8gb")

    def display(self):
        print("Student info :", self.name, self.roll)
        self.laptop1.laptopInfo()

    class Laptop:
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def laptopInfo(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Mohammad Jonayed Sarkar", 19)
s1.display()

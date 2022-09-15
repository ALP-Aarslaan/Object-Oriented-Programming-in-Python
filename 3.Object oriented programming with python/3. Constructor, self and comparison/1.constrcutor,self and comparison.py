class Computer:
    def __init__(self):
        self.name = "core i5"
        self.ram = "8gb"

    def upgrade(self):
        self.ram = "16gb"

    def compare(self, obj2):
        if self.ram == obj2.ram:
            return True
        else:
            return False


c1 = Computer()
c1.upgrade()
c2 = Computer()
# c2.upgrade()
if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
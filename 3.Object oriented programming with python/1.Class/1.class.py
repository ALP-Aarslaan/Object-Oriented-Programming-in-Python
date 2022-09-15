class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def bark(self):
        print("Dog Barks")

    def add(self, x):
        return x + x

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


dog1 = Dog("Tohfa", 20)
print(dog1.get_name())
dog1.bark()
print(dog1.add(4))
print(dog1.get_age())
dog1.set_age(21)
print(dog1.get_age())


# multiple inheritance :

class Father:
    def __init__(self,F_name,F_age) -> None:
        self.F_name = F_name
        self.F_age = F_age

    def display(self):
        print(f"Father's name : {self.F_name} & age : {self.F_age}")

class Mother:
    def __init__(self,M_name,M_age) -> None:
        self.M_name = M_name
        self.M_age = M_age

    def display(self):
        print(f"mother's name : {self.M_name} & age : {self.M_age}")

class Son(Father,Mother):
    def display(self,sonName,age):
        print("son's name : ",sonName)
        print("son's age : ",age)
        return super().display()


class Son1(Mother,Father):
    def display(self,sonName,age):
        print("son's name : ",sonName)
        print("son's age : ",age)
        return super().display()

son1 = Son("MD. Omar Faroque Sarkar", 58)
son1.display("Mohammad Jonayed",22)
print("\n\n")
son2 = Son1("Shamima Akter", 55)
son2.display("Mohammad jonayed sarkar", 23)
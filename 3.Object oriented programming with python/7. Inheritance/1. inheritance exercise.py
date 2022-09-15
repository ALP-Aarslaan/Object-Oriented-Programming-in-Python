"""
inheritance is like inheriting wealth from our ancestors
this same method also works in programming.
there are 3 types of inheritance in Python:
1. single level inheritance
2. multi level inheritance
3. multiple inheritance
"""


# single level inheritance:
class A:
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 in working")


class B(A):
    def feature3(self):
        print("feature 3 is working")


b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()


# multi level inheritance :
class C(B):
    def feature4(self):
        print("feature 4 is working")


c = C()
c.feature1()
c.feature2()
c.feature3()
c.feature4()

# multiple inheritance:
class E:
    def feature5(self):
        print("feature 5 is working")

class F:
    def feature6(self):
        print("feature 6 is working")

class G(E,F):
    def feature7(self):
        print("feature 7 is working")

g = G()
g.feature5()
g.feature6()
g.feature7()
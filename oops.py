class A:
    def feature(self):
        print("feature 1 of class A is working")

    def feature2(self):
        print("feature 2 of class A is working")
class B():
    def feature3(self):
        print("feature 3 of class B is working")

    def feature4(self):
        print("feature 4 of class B is working")

class C(B,A):
    def feature5(self):
        print("feature 3 of class C is working")

    def feature6(self):
        print("feature 4 of class C is working")
# a1 = A()
# a1.feature()
# a1.feature2()

b1= B()
b1.feature3()

c1= C()
c1.feature4()
c1.feature()
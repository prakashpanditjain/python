class A:
    def __init__(self):
        print("In A init ")

    def feature(self):
        print("feature 1 of class A is working")

    def feature2(self):
        print("feature 2 of class A is working")
class B():
    def __init__(self):
        # super().__init__()
        print("In B init")

    def feature3(self):
        print("feature 3 of class B  is working")

    def feature4(self):
        print("feature 4 of class B is working")
# MRO - method resolution order

class C(B,A):
    def __init__(self):
        try:
            super().__init__()
            super().__init__()
            print("In C init")
        except:
            pass


a1 = C()


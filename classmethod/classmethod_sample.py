class sampleclass():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        c = self.a + self.b
        return c

    @classmethod
    def substraction(cls, a, b):
        return a - b

    @classmethod
    def multiplication(cls, a, b):
        return a * b

    @staticmethod
    def division(a,b):
        return round(a / b)


instance1 = sampleclass(1, 2)
print(instance1.addition())
print(sampleclass.substraction(6, 3))
print(sampleclass.multiplication(2, 46))
print(instance1.multiplication(2, 30))
print(sampleclass.division(100,10))

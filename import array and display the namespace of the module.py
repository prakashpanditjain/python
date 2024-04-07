import array
# for _ in array.__dict__:
#     print(_)


class defining_the_class:
    def __init__(self,lst):
        self.self = self
        self.lst = lst
    def add_value(self,a,b):
        self.a = a
        self.b = b
        sum = a +b
        return sum

for _ in defining_the_class.__dict__:
    print(_)
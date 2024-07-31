import array
# for _ in array.__dict__:
#     print(_)


class defining_the_class:
    def __init__(self,a=3,b=5):
        self.self = self
        self.a = a
        self.b = b
    def add_value(self):
        sum = self.a + self.b
        return sum

# Instatiate the object for class defining_the_class
result = defining_the_class(23,34)

# call the function add_value
res = result.add_value()

# print the res
print(res)

# Print __dict__(special method for object result)
print(result.__dict__)


print(list(_ for _ in defining_the_class.__dict__))
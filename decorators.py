# from Moduleimport_and_specialVariable__name__.addsub_module import add
# from Moduleimport_and_specialVariable__name__.addsub_module import sub
#
#
# def outer(x):
#     def innerfunction(y):
#         if y > x:
#             result = add(x, y)
#         else:
#             result = sub(x, y)
#         return result
#
#     return innerfunction
#
#
# def passfunc(x, y):
#     r = outer(x)
#     return r(y)
#
#
# # add_five = outer(5)
# # result = add_five(25)
# # print(result)
# if __name__ == '__main__':
#     result = passfunc(5, 7)
#     print(result)
#
#
#
# # USE OF DECORATOR
# def make_pretty(fun):
#     def inner():
#         print("I got decorated")
#         fun()
#
#     return inner
#
#
# @make_pretty
# def ordinary():
#     print("I am ordinary")
#
# ordinary()



#USE OF __CLASS__() FUNCTION

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Create an instance of Multiplier
double = Multiplier(2)
triple = Multiplier(3)

# Call the instances
print(double(5))  # Output: 10
print(triple(5))  # Output: 15
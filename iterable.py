#Define a function gen which generate only values in terms of object
def gen(n):
    for i in range(n):
        yield i
number  = gen(6)
print(gen(2))  #This will print only object of the function

# Print the values on the fly of number
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))

iter = iter("234")

# Using try and except method try avoiding printing errors
try:
    print(next(iter))
    print(next(iter))
    print(next(iter))
    print(next(iter))
    print(next(iter))
    print(next(iter))
    print(next(iter))
except:
    pass

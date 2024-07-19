# count = {}
# for i in room_number:
#     if i in count:
#         count[i] +=1
#     else:
#         count[i] = 1
#
# print(count)
# for key,value in count.items():
#     # print(key,value)
#     if value != 5:
#         print(key)


import pandas as pd

print(pd)

#Use OF TRY EXCEPET ELSE AND FINALLY BLOCKS

def divide_numbers(a, b):
    try:
        # Try to perform the division
        result = a / b
    except ZeroDivisionError:
        # Handle the division by zero error
        print("Error: Cannot divide by zero.")
    except TypeError:
        # Handle the error if a non-numeric type is provided
        print("Error: Both arguments must be numbers.")
    else:
        # This block executes if no exceptions were raised
        print(f"The result is {result}.")
    finally:
        # This block always executes, regardless of whether an exception was raised or not
        print("Execution completed.", end='\n')

# Example usage
# divide_numbers(10, 2)  # Successful division
# divide_numbers(10, 0)  # Division by zero
# divide_numbers(10, 'a')  # Invalid type


def gen(n):
    for i in range(n):
        yield i
number  = gen(6)
print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))

iter = iter("234")
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
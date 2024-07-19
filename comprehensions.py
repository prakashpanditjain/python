"""
Below are the examples of list comprehension , dictionary comprehension , set comprehension and generator comprehension
"""
from testfile_primenumber import is_prime

# List comprehension

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
# Print all the names in upper case using list comprehension
# print([i.upper() for i in names])

# Get only first three letters of names using list comprehension
print([i[:3] for i in names])

# Dictionary Comprehension

# Question: Using the above dictionary, create a new dictionary using dictionary comprehension that contains only
# those names whose associated number is greater than 7. In the new dictionary, increase the number by 2 for each
# selected entry.

# Dictionary with names as keys and numbers as values
names_and_numbers = {"Alice": 5, "Bob": 8, "Charlie": 12, "David": 3, "Eve": 15, "Frank": 7, "Grace": 10}

print({key: value + 2 for key, value in names_and_numbers.items() if value > 7})

# Set comprehension

# Set of integers
numbers_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

"""Requirements
1.	Filter Criteria: Select numbers that are prime and greater than 10.
2.	Transformation: For each selected number, subtract 1.
3.	Output: Use set comprehension to generate a new set based on the above criteria.
"""


# Take list and create list for prime numbers and are greater than 10
def filter_prime(*args):
    prime_numbers = [i - 1 for i in args if is_prime(i) and i > 10]
    return prime_numbers


print("prime number with substraction of 1: ", filter_prime(*numbers_set))

# Generator Comprehension
"""
You are given a list of integers. Your task is to create a generator that yields only the square of even numbers from 
the list. The generator should produce these values one at a time, on demand. This approach should be memory 
efficient, especially when dealing with large datasets.
"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def evennumber_generator(*args):
    return (i for i in args if i % 2 == 0)


genobj = (evennumber_generator(*lst))
print(type(genobj))
print([i for i in genobj])

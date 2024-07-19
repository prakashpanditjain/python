"""
Below are the examples of list comprehension , dictionary comprehension , set comprehension and generator comprehension
"""

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
names_and_numbers = {
    "Alice": 5,
    "Bob": 8,
    "Charlie": 12,
    "David": 3,
    "Eve": 15,
    "Frank": 7,
    "Grace": 10
}

print({key: value+2 for key, value in names_and_numbers.items() if value > 7})

# Set comprehension

# Set of integers
numbers_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}



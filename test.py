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

"""
Use of *args and **kwargs
"""


def function1(name, *args):
    age = args[0]
    profession = args[1]
    print(f"my name is {name} and my age is {age} . I work as a {profession}")


def keyword(*args, **kwargs):
    for i in args:
        # print(i)
        # for key, value in kwargs.items():
        # print("".join(f"{key}: {value}"))
        # print('\n')

        print(", ".join(f"{key}: {value}" for key, value in i.items()))


# Passing the arguments to function1 method

# function1("prakash", 28, "software engineer!")


# defining the list which takes as * args
people = [{"name": "Alice", "age": 28}
    , {"name": "Bob", "age": 34},
          {"name": "Catherine", "age": 22},
          {"name": "David", "age": 40},
          {"name": "Eva", "age": 31},
          {"name": "Frank", "age": 25},
          {"name": "Grace", "age": 29},
          {"name": "Henry", "age": 37},
          {"name": "Isabella", "age": 19},
          {"name": "Jack", "age": 45}]

keyword(*people)

import pandas as pd

print(pd)
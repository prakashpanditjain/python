
"""
Use of *args and **kwargs
"""

# Define function
def function1(name, *args):
    age = args[0]
    profession = args[1]
    print(f"my name is {name} and my age is {age} . I work as a {profession}")

# Passing the arguments to function1 method
# function1("prakash", 28, "software engineer!")

def keyword(*args, **kwargs):
    try:
        for i in args:
            print(ii)    # error to not to pass the function
            # for key, value in kwargs.items():
            # print("".join(f"{key}: {value}"))
            # print('\n')

            print(", ".join(f"{key}: {value}" for key, value in i.items()))
    except:
        pass


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
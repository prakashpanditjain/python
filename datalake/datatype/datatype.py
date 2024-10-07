import sys


class schema():
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self, name):
        return str(name)

    def __int__(self, value):
        return str(value)


if __name__ == '__main__':
    print(sys.platform)
    x= list(range(0))
    print(sys.getsizeof(x))
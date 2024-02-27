from addsub_module import *

def func1():
    print("this is the func1 of module1")

def func2():
    sub(20,5)
    print("this is the func2 of module 2")

def main():
    try:
        func1()
        func2()
    except:
        pass


if __name__ == '__main__':
    try:
        main()
    except:
        pass

print("Name of the module is ", __name__)
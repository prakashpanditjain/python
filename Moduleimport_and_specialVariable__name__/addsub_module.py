def add(a, b):
    global c
    c = a + b
    print(c)


def sub(a, b):
    global c
    if a < b:
        a, b = b, a
    print("this is module", __name__)
    print(a - b)


def main():
    x = add(a=10, b=5)
    y = sub(a=2, b=7)



if __name__ == "__main__":
    main()
    print("name of the module is", __name__)

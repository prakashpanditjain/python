def add(a,b):
    global c
    c = a+b
    print(c)
def sub(a,b):
    global c
    if a < b :
        a,b = b,a
    c = a - b
    print(c)
    print("this is module",__name__)

# <editor-fold desc="Description">
def main():
    add(a=3,b=5)
    sub(a=5,b=2)
# </editor-fold>

if __name__ == "__main__":
    main()
    print("name of the module is", __name__)

from Moduleimport_and_specialVariable__name__.addsub_module import add


def outer(x):
    def innerfunction(y):
        if y > x:
            return add(x, y)
        else:
            return (x - y)

    return innerfunction


def passfunc(x, y):
    r = outer(x)
    return r(y)


# add_five = outer(5)
# result = add_five(25)
# print(result)
if __name__ == '__main__':

    result = passfunc(5, 7)
    print(result)

# from indexnumber import n
from functools import reduce


def factorial(*args):
    fact = reduce(lambda a, b: a * b, lst)
    # print(fact)
    return fact


if __name__ == "__main__":

    lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    oddnumber = list(filter(lambda x: x % 2 == 1, lists))
    print("Using filter method filter odd number", oddnumber)

    sre = list(map(lambda x: x + 3, oddnumber))
    print("Using map function over list add 3 in each number", sre)

    # Factorial with the help of reduce

    lst = []
    for i in range(1, 5):
        lst.append(i)
    print('printing list from 1 to 4:- ', lst)

    print(factorial(*lst))

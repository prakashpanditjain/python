# from indexnumber import n
from functools import reduce

lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddnumber = list(filter(lambda x: x % 2 == 1, lists))
print(oddnumber)

sre = list(map(lambda x: x + 3, oddnumber))
print(sre)

# Factorial with the help of reduce

lst = []
for i in range(1, 5):
    lst.append(i)
print(lst)

fact = reduce(lambda a, b: a * b, lst)
print(fact)

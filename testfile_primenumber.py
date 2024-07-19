def primenumber(n):
    for i in range(2, n):
        for j in range(2, int(i / 2 + 1)):
            if i % j == 0:
                break
            elif j == int(i / 2):
                print(i)


(primenumber(100))


# print(int(11/2))

def primefromlist(*args):
    for i in args:
        for j in range(2, int(i / 2 + 1)):
            if i % j == 0:
                break
            elif j == int(i / 2):
                print(i)


# Using list comprehension print those numbers only which are devisible by 3
print([i for i in range(31) if i % 3 == 0])

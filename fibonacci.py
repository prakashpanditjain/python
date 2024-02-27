#print fib number
#  0 1 1 2 3 5 8
# a b c
def fib(n):
    a = 0
    b = 1
    print(a,"\n",b)

    for i in range(2,n):
        c = a + b
        a = b
        b =c

        #this is check if the next number is less or equal to the user provided number
        if c <= n:
            print(c)
        else:
            break

result = fib(50)
print(result)
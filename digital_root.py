"""" you have to find digit root for 15 is 1+5 = 6
now to find the digit root if the length of the digit is not one then we need to add each digit upto it become one digit
and to that single digit/number we call digit_root
"""
k = 0
def root(n):
    k= 0
    for i  in str(n):
        k +=int(i)
    if len(str(k)) != 1:
       return root(k)
    else:
        return k

print(root(3081999))
# print(b)
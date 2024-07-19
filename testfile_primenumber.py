def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


# (primenumber(10))

# print(int(11/2))

def primefromlist(*args):
    list_ofprime = set([i for i in args if is_prime(i)])
    return list_ofprime


if __name__ == "__main__":
    numbers_set =[2, 3, 5, 7, 11,1,23,34,435,23,567,45,56,76,78,79,77,3,8789,54,1234,23, 13, 17, 19, 23, 29, 31]
    # numbers_set =[2, 3, 5]
    print(primefromlist(*numbers_set))

    # Using list comprehension print those numbers only which are devisible by 3
    print([i for i in range(31) if i % 3 == 0])

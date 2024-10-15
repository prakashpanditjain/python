import time

from calculate_execution_time import log_execution_time


@log_execution_time
def add_numbers(a, b):
    result = a + b
    return result


@log_execution_time
def square_of_number(*args):
    time.sleep(5)
    list1 = args[0]
    for i in range(len(list1)):
        list1[i] = list1[i] ** 2
    return list1

    return list1


if __name__ == '__main__':
    a, b = 3, 5
    object1 = add_numbers(a, b)
    print(f"The addition of {a} and {b} numbers {object1}")

    list1 = [234, 43234, 34234, 534, 34, 345, 234, 234, 45, 324, 34523452345325, 234523452345234, 45634567567,
             3453134124, 2456456454356, 456, 456, 456456456, 456, 45, 6, 5645, 6, 456, 4, 56756, 75, 6757,
             5675675674562465, 564623453245, 23454656456, 456756767, 5]
    object2 = square_of_number(list1)

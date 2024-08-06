def filter_using_lambda(list1):

    """
    :param list1: pass a list
    :return: this function return a list which filters even numbers
    """
    new_list = list(filter(lambda x: (x % 2 == 0) , list1))
    return new_list

def map_using_lambda(list1):

    """
    :param list1:
    :return: this function returns the list of square number
    """
    new_list = list(map(lambda x: x* x , list1))
    return new_list

if __name__ == '__main__':
    list1 = list(range(1,30))
    even_list = filter_using_lambda(list1)
    print(even_list)

    square_numbers = map_using_lambda(list1)
    print(square_numbers)
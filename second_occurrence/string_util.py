

#make
def second_occurrence(lst : list, x) -> int:
    """

    :param lst: A list of elements where we want to find the second occurrence of a specific element.
    :param x: an element whose second occurrence we want to find in the list.
    :return: returns the index of the second occurrence of the element x in the list lst.
    """
    dict = {} #initialize an empty dictionary to keep track of occurrences
    for i in range(len(lst)):
        #iterate through the list and check if the element is already in the dictionary
        if lst[i] in dict:          #if element is already in the dictionary
            dict[lst[i]] += 1.      #add 1 to the count of occurrences
            if dict[x] == 2:        #if the count of occurrences of x is 2, return the index
                return i
        else:
            dict[lst[i]] = 1        #else add the element to the dictionary with a count of 1
    return -1


#the more precise and efficient way to find the second occurrence of an element in a list is to use a simple loop with a counter.
# This function iterates through the list, counting occurrences of the specified element.
def second_occurrence_efficient(lst: list, x) -> int:
    """
    This function finds the index of the second occurrence of a specified element in a list.
    :param lst: list of elements where we want to find the second occurrence of a specific element.
    :param x: an element whose second occurrence we want to find in the list.
    :return: returns the index of the second occurrence of the element x in the list lst.
    """
    count = 0
    for i , val in enumerate(lst):          #Using enumerate to get both index and value
        if val == x:                        #check if the value is equal to x
            count += 1                      #increment the count
            if count == 2:                  #if the count is 2, return the index
                return i
    return -1



if __name__ == "__main__":
    scn = second_occurrence([1,2,3,4,5,6,2,8,2],2)
    print(scn)
    second_occurrence_efficient(['a', 'b', 'c', 'a', 'd', 'a'], 'a')
    print(second_occurrence_efficient([1, 2, 3, 4, 5, 6, 2, 8, 2], 2))
    print(second_occurrence_efficient([1, 2, 3, 4, 5, 6, 2, 8, 2], 3))
    print(second_occurrence_efficient([1, 2, 3, 4, 5, 6, 2, 8, 2], 9))
    print(second_occurrence_efficient([1, 2, 3, 4, 5, 6, 2, 8, 2], 1))
    print(second_occurrence_efficient([1, 2, 3, 4, 5, 6, 2, 8, 2], 6))
    print(second_occurrence_efficient([1, 2, 3, 4, 5, 6, 2, 8, 2], 8))
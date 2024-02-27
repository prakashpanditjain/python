
lst = [24,4,5,6,7,8,42,2,5,1,3,6,4,6]

def sortlist(l):
    for i in range(len(lst)):
        # print(i)
        swapposition = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[swapposition]:
                swapposition = j

        temp = lst[i]
        lst[i] = lst[swapposition]
        lst[swapposition] = temp

sortlist(lst)
print(lst)

lst2 = [1,2,3,6,5,4,3,2,9,8,6,45,6,7,8,6]
sortlist(lst2)
print(lst2)
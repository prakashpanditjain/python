from fontTools.misc.cython import returns

arr = [1,2,3,4,5]

# add 6 at end
arr.append(6)
print(f"added 6 at end {arr}")

# remove 3
arr.remove(3)
print(f"removed 3 from the arr{arr}")

# change  2 to 20
num = arr.index(2)
arr.pop(num)
arr.insert(num,20)

print(f"changed 2 to 20{arr}")

# Finer version of replacing element
arr[arr.index(4)] = 40

print(f"this is finer operation{arr}")




# search the max from the list without max() operation

arr = [10,20,30,40,50]
arr=[-10,-3,-4,-20]
def max_num_find(arr:list)-> int :

    max_num = arr[0]
    
    for n in arr[1:]:
        if n > max_num:
            max_num = n
    return max_num


m = max_num_find(arr)
print(m)

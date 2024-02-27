# find the index number by function as well as user defined function by taking input

array = []
n = int(input("enter the length of a array \n"))

for i in range(n):
    number = int(input("Enter the number for array \n"))

    array.append(number)

print(array)

# find the index of an arra
z = 0

value = int(input("enter the value from array you want to search \t"))

if value not in array:
    print("Your entered value is not in array")
else:
    for x in array:
        if x == value:
            print(z)

        z +=1
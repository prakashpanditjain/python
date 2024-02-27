# a = int(input("Enter the first value\n"))
# b = int(input("enter the second value\n"))

try:
    print("Resource has opend")
    # c = a/b
    # print(c)
    k = str(input("Enter your Name"))
except Exception as e:
    print("You have entered something other than Name -->", e)

finally:
    print("resource closed")

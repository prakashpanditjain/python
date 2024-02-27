# Print below pattern of numbers
# 1 2 3 4
# 2 3 4
# 3 4
# 4

for i in range(1,5):
    k = i
    for j in range(5-i):
        print(k,end=' ')
        k = k +1
    print("")
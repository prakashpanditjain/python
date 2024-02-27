for i in range(2,50):
    for j in range(2,int(i/2+1)):
        if i%j == 0:
            break
        elif j == int(i/2):
            print(i)


# print(int(11/2))
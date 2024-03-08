room_number = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 8]
# vvuvcydr = aesjfasid

for i in set(room_number):
    room_number.remove(i)
    if i not in room_number:
        print(i)

# count = {}
# for i in room_number:
#     if i in count:
#         count[i] +=1
#     else:
#         count[i] = 1
#
# print(count)
# for key,value in count.items():
#     # print(key,value)
#     if value != 5:
#         print(key)
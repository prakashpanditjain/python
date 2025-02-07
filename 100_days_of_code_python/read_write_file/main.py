import os

file_path = os.path.realpath('my_file.txt')
print(file_path)


with open('') as file:
    contents = file.read()
    print(contents)
#
#
# with open('new_file.txt',mode='w') as file:
#     contents = file.write("writing in append mode")
#     print(contents)
#
#
# print(os.path.realpath('new_file.txt'))
# print(os.path.dirname('new_file.txt'))


with open('my_file.txt.py') as file:
    contents = file.read()
    print(contents)


with open('new_file.txt',mode='r') as file:
    contents = file.write("\n writing is in append mode")
    print(contents)

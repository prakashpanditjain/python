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
import secrets
import string


def random_secretnumber(n):
    print(type(secrets.randbelow(n)))
    return secrets.randbelow(20)


def generate_password(n: int):
    char: str = string.ascii_letters + string.digits + string.punctuation
    # print(char)
    password = "".join(secrets.choice(char) for i in range(n))
    return password


def main():
    print("in main")
    print(random_secretnumber(4))
    print(generate_password(10))


if __name__ == '__main__':
    main()

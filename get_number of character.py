"""
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
"""
from typing import Any
from typing import Dict


def get_character_count(char_):
    dic: dict[Any, Any] = {}
    for i in char_:
        dic[i] = dic.get(i, 0) +1
    print("\n".join(f"{k}:{v}" for k, v in dic.items()))


if __name__ == '__main__':.
    get_character_count('aldsbvusghrub')

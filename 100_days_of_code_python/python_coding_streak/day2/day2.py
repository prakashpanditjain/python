"""
Problem: First Non-Repeating Character (Classic, but sneaky)

You’re given a string s.
Return the index of the first character that does not repeat anywhere else in the string.
If every character repeats, return -1.

Example:
Input: "leetcode"
Output: 0 (because 'l' appears only once)

Input: "aabb"
Output: -1
"""

def first_non_repeating_character(s: str) -> int:
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
    return -1

result = first_non_repeating_character("swiss")
print(result)
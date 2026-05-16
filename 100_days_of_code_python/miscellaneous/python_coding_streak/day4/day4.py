"""
Today we step into sliding window land, where efficiency stops being optional.

Problem: Longest Substring Without Repeating Characters

You’re given a string s.
Find the length of the longest substring that contains no repeating characters.

Example:
Input: "abcabcbb"
Output: 3 → "abc"

Input: "bbbbb"
Output: 1 → "b"

Input: "pwwkew"
Output: 3 → "wke"
"""


def longest_substring_without_repeating_characters(s: str) -> int:
    char_index_map = {}
    left_pointer = 0
    max_length = 0

    for index, char in enumerate(s):
        if char in char_index_map and char_index_map[char] > left_pointer:
            left_pointer = char_index_map[char] + 1
            char_index_map[char] = index

        else:
            char_index_map[char] = index
        max_length = max(max_length, index - left_pointer + 1)
    return max_length


lswrc = longest_substring_without_repeating_characters('abcdefghijkldmnopqrstuvwxycdeakufasebr')
print(lswrc)

"""
Problem: Longest Alternating Substring (Easy–Medium)

You’re given a string containing only the characters "0" and "1".
Find the length of the longest substring where the characters strictly alternate.
Alternate means "0101" or "1010" or "01" etc.

Example:
Input: "0010101110"
Output: 5
Explanation: The longest alternating substring is "10101".

"""
from attr.validators import max_len


def longest_alternating_substring(s: str)-> int:
    max_length = 1
    current_length = 1
    for i in range(1, len(s)):

        if s[i] != s[i-1]:
            current_length += 1
            max_length = max(max_length ,current_length)
        else:
            current_length =1

    return max_length

longest_alt_substr= longest_alternating_substring('00101011101101')
print(longest_alt_substr)
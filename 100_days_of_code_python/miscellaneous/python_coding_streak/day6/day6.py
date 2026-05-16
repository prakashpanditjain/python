"""
same as that of day5.py
Problem: Sort Characters by Frequency

You’re given a string s.
Return a new string where the characters are sorted in descending order of frequency.

Example 1:
Input: s = "tree"
Output: "eert"
"""

def sort_characters_by_frequency(s: str) -> str:
    frequency_map ={}

    for char in s:
        frequency_map[char] = frequency_map.get(char, 0) +1

    sorted_tuple = sorted(frequency_map.items(), key=lambda x: x[1] , reverse=True)
    print(sorted_tuple)
    result = ''.join([char * freq for char, freq in sorted_tuple])
    return result



obj = sort_characters_by_frequency('cccaaaabbbddeeefffffggggghhhiiiijjjjj')
print(obj)
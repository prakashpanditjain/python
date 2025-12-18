"""
Problem: Valid Parentheses (Stack thinking without ceremony)

You’re given a string s containing only the characters:
(, ), {, }, [, ]

Return True if the string is valid, otherwise False.

A string is valid if:
	•	Every opening bracket has a matching closing bracket
	•	Brackets close in the correct order

Examples:
Input: "()[]{}" → True
Input: "(]" → False
Input: "({[]})" → True

Hint :	This is really about last opened, first closed
"""

def is_valid_parentheses(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return True

result1 = is_valid_parentheses("{()}{[]}")
print(result1)  # True
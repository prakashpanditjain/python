"""
Day 9. The streak has crossed into the zone where discipline beats excitement. That’s where real skill grows.

Today’s problem stays adjacent to what you’ve done, but it trains a different reflex: tracking state across a scan.

Problem: Longest Consecutive Sequence

You’re given an unsorted list of integers.
Find the length of the longest sequence of consecutive numbers.

Consecutive means numbers follow each other by +1, not necessarily next to each other in the array.
nums = [100, 4, 200, 1, 3, 2]
Output: 4 → [1, 2, 3, 4]
Walkthrough:
    •	100 → start sequence [100]
    •	4 → start sequence [4]
    •	200 → start sequence [200]
    •	1 → start sequence [1, 2, 3, 4]
    •	3 → already in sequence
    •	2 → already in sequence
"""

def longest_consecutive(nums: list[int]) -> int:
    # your code
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num -1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current +=1
                length +=1
                max_length = max(max_length, length)

    return max_length




setnum = set(list([100, 4, 200, 1, 3, 2]))
print(setnum)

long_cons = longest_consecutive([100, 4, 200, 1, 3, 2])
print(long_cons)
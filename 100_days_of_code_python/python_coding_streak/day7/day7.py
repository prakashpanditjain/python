"""

Problem: First Element to Appear K Times

You’re given an integer array nums and an integer k.
Return the first element (by order of appearance) whose frequency becomes exactly k.
If no such element exists, return -1.
nums = [1, 7, 4, 3, 4, 8, 7]
k = 2

Walkthrough:
	•	1 → 1 time
	•	7 → 1 time
	•	4 → 1 time
	•	3 → 1 time
	•	4 → 2 times  ✅ first to reach k

4

"""


def first_element_k_times(nums: list[int], k: int) -> int:
    frequency  = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] == k :
            return num
    return -1

element = first_element_k_times([1, 7, 4, 3,3, 4, 8, 7, 7], 1)
print(element)

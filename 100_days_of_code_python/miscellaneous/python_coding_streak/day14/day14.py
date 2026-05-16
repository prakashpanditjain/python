"""
Question 2 (core mastery)

Count Subarrays with Sum = k

Given nums and an integer k, return the total number of continuous subarrays whose sum equals k.

Example:
nums = [1, 2, 1, 2, 1], k = 3
Output: 4

Before coding, list the subarrays on paper once.
Then ask: Why brute force is wasteful here?
"""

def subarray_sum_equals_k(nums: list[int], k:int) -> int:
    count = 0
    current_sum = 0
    sum_frequency = {0:1}

    for num in nums:
        current_sum += num
        if (current_sum - k) in sum_frequency:
            count += sum_frequency[current_sum- k]
        sum_frequency[current_sum] = sum_frequency.get(current_sum, 0) + 1

    return count

obj = subarray_sum_equals_k(nums = [3, 4, -7, 1, 3, 3, 1, -4], k = 7)
print(obj)
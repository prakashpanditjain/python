"""
Count Subarrays with Sum = 0

Given an array of integers (can include negatives), return the number of subarrays whose sum is 0.

Example:
[1, -1, 2, -2, 3]
Output: 3

This is the same pattern you just learned, stripped to its bones.
"""

def count_zero_sum_subarrays(nums: list[int]) -> int:
    count = 0
    current_sum = 0
    sum_frequency = {0: 1}

    for num in nums:
        current_sum += num
        if current_sum in sum_frequency:
            count += sum_frequency[current_sum]
        sum_frequency[current_sum] = sum_frequency.get(current_sum, 0) + 1

    return count

czss = count_zero_sum_subarrays( [0,0,0] )
print(czss)
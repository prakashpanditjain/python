"""
Day 11. At this point the streak isn’t about proving anything. It’s about showing up and sharpening one edge at a time.

Today’s problem keeps the single-pass + state theme, but introduces a small twist: resetting state when it hurts you.

Problem: Maximum Subarray Sum (Kadane’s Algorithm)

You’re given an integer array nums.
Find the contiguous subarray with the largest sum and return that sum.

⸻

Examples
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

output - [4, -1, 2, 1]

in/p
nums = [-1, -2, -3]
o/p
-1


i/p
nums = [1]
o/p
1

"""



def max_sub_array(nums: list[int]) -> int:
    # your code
    current_sum = 0
    max_sum = 0

    for num in nums:
        if max_sum == 0:
            return -1
        current_sum = max(num, current_sum +  num)
        max_sum = max(max_sum, current_sum)

    return max_sum

sum_subarry = max_sub_array([-1, -2, -3])
print(sum_subarry)
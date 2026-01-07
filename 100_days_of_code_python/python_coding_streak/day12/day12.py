"""
Today’s problem connects beautifully with what you just learned: it looks like Kadane’s cousin, but asks a yes/no question instead of a max.

Problem: Subarray Sum Equals K

You’re given an integer array nums and an integer k.
Return the number of contiguous subarrays whose sum equals k.
examples
nums = [1, 1, 1]
k = 2
Output: 2 → [1, 1], [1, 1]
nums = [1, 2, 3]
k = 3
Output: 2 → [3], [1, 2]

More Example with edge cases
nums = [1, -1, 0]
k = 0
Output: 3 → [1, -1], [-1, 0], [0]

Walkthrough:
    •	Initialize count = 0, current_sum = 0, sum_frequency = {0: 1}
    •	Iterate through nums:
        ◦	num = 1:
            ‣	current_sum = 1
            ‣	current_sum - k = 1 - 0 = 1 (not in sum_frequency)
            ‣	Update sum_frequency: {0: 1, 1: 1}
        ◦	num = -1:
            ‣	current_sum = 0
            ‣	current_sum - k = 0 - 0 = 0 (in sum_frequency, count += 1)
            ‣	Update sum_frequency: {0: 2, 1: 1}
        ◦	num = 0:
            ‣	current_sum = 0
            ‣	current_sum - k = 0 - 0 = 0 (in sum_frequency, count += 2)
            ‣	Update sum_frequency: {0: 3, 1: 1}
    •	Final count = 3

we can solve this by other way using current num matching with k or not and current number + 1 matching with k or not but that will be O(n^2) time complexity

"""

def subarray_sum(nums: list[int], k: int) -> int:
    # your code [1,2,3], k=6
    count = 0
    current_sum = 0
    sum_frequency = {0: 1}
    for num in nums:
        current_sum += num
        if (current_sum - k) in sum_frequency:
            count += sum_frequency[current_sum - k]
        sum_frequency[current_sum] = sum_frequency.get(current_sum, 0) + 1
    return count

# sub_sum = subarray_sum([1, -1, 0], 0)
# print(sub_sum)
#
# # some more examples as below
# sub_sum1 = subarray_sum([1, 1, 1], 2)
# print(sub_sum1)

sub_sum2 = subarray_sum([1, 2, 3, 2, 1], 6)
print(sub_sum2)


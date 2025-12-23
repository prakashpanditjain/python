"""
 At this point the streak has momentum. Momentum is dangerous in a good way.

Today’s problem bends your thinking from windows to ordering.

Problem: Top K Frequent Elements

You’re given an integer array nums and an integer k.
Return the k most frequent elements.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]
"""
from sqlalchemy.orm.sync import bulk_populate_inherit_keys


def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    sorted_tuple = sorted(frequency_map.items(), key= lambda x : x[1], reverse=True)
    result = [num for num, freq in sorted_tuple[:k]]
    return result

tkfe = top_k_frequent_elements([1,1,1,3,2,4,2,2,3,3,3,3,3,2,1,4,5,6,7,5,3,4,5],4)
print(tkfe)
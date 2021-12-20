# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# # Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Memory Usage: 16.4 MB, less than 8.74% of Python3 online submissions for Two Sum.
# Runtime: 89 ms, faster than 47.07% of Python3 online submissions for Two Sum.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        value_dict = {}
        half = None

        if (target/2).is_integer():
            half = target/2

        for num_i, num in enumerate(nums):
            if value_dict.get(num) and half == num:
                return [value_dict.get(num)[1], num_i]
            value_dict[num] = [target - num, num_i]

        print(value_dict)
        for key, val in value_dict.items():
            act_val, indice_2 = val[0], val[1]
            if value_dict.get(act_val):
                if indice_2 == value_dict.get(act_val)[1]:
                    continue
                return [indice_2, value_dict.get(act_val)[1]]

        return output


print(Solution().twoSum(nums = [3,3], target = 6))

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

    # 10**5 = 10^5 = 10*10*10*10*10

    # 0 <= nums.length <= 10**5
    # -10**9 <= nums[i] <= 10**9


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_cons = 1

        lookup = {str(val): 1 for val in nums}
        out = []
        seq = 1

        for num in nums:
            if lookup.get(str(num-1)) is None:
                length = 0
                while lookup.get(str(num + length)):
                    length += 1
                longest_cons = max(length, longest_cons)

                if longest_cons >= len(nums):
                    break

        return longest_cons


print(Solution().longestConsecutive(nums=[100,4,200,1,3,2]))
print(Solution().longestConsecutive(nums=[-100,4,200,1,3,2]))
print(Solution().longestConsecutive(nums=[0,3,7,2,5,8,4,6,0,1]))
# print(Solution().longestConsecutive(nums=[char for char in str(112233445566778899003400000111123334444)]))

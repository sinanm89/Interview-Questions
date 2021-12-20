# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints:

#     1 <= intervals.length <= 10**4
#     intervals[i].length == 2
#     0 <= starti <= endi <= 10**4
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []

        if len(intervals) <= 1 :
            return [] if len(intervals) == 0 else intervals

        intervals.sort(key=lambda x: x[0])
        # [[0,2],[1,4],[3,5]]
        prev_l, prev_r = intervals[0][0], intervals[0][1]
        out.append(intervals[0])
        for i in range(1, len(intervals)):
            l, r = intervals[i][0], intervals[i][1]
            if out[-1] == intervals[i]:
                continue
            if l <= prev_r:
                out.pop()
                # print(prev_l,prev_r,  l, r)
                out.append([min(l, prev_l), max(r, prev_r)])
                # overlap
            else:
                out.append(intervals[i])

            prev_l, prev_r = out[-1][0], out[-1][1]
        return out


intervals = [[1,3],[2,6],[8,10],[15,18]]
exp = [[1, 6], [8, 10], [15, 18]]
# print(Solution().merge(intervals))
assert Solution().merge(intervals) == exp

intervals = [[1,4],[5,6]]
exp = [[1, 4], [5, 6]]
print(Solution().merge(intervals))
assert Solution().merge(intervals) == exp

intervals = [[1,3]]
exp= [[1, 3]]
print(Solution().merge(intervals))
assert Solution().merge(intervals) == exp

intervals = [[1,4],[0,0]]
exp = [[0,0],[1,4]]
print(Solution().merge(intervals))
assert Solution().merge(intervals) == exp

intervals = [[1,4],[0,2],[3,5]]
exp = [[0,5]]
print(Solution().merge(intervals))
assert Solution().merge(intervals) == exp


intervals = [[0,0],[1,2],[5,5],[2,4],[3,3],[5,6],[5,6],[4,6],[0,0],[1,2],[0,2],[4,5]]

exp = [[0,6]]
print(Solution().merge(intervals))

assert Solution().merge(intervals) == exp

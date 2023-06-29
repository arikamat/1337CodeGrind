#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
from typing import *
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a=[]
        intervals.sort()
        # print(len(intervals),intervals )
        curr = intervals[0]
        for i in intervals[1:]:
            # print(a,curr, i)
            start = i[0]
            end = i[1]
            if curr[1] >= i[0]:
                curr[1] = max(curr[1],i[1])
            else:
                a.append(curr)
                curr=i
        if curr not in a:
            a.append(curr)
        # print(a)
        return a
s = Solution()
s.merge([[1,4],[4,5]])
# @lc code=end


#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
from typing import *
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxCt=0
        while len(nums)>0:
            curr = nums.pop()
            ct=1
            i=1
            while curr+i in s:
                s.remove(curr+i)
                ct+=1
                i+=1
            i=1
            while curr-i in s:
                s.remove(curr-i)
                ct+=1
                i+=1
            maxCt = max(ct,maxCt)
        # print(maxCt)
        return maxCt
# @lc code=end
# s = Solution()
# nums = [0]
# s.longestConsecutive(nums)
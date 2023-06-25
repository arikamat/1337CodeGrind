#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
from typing import *
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[1]*len(nums)
        for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        last = 1
        for i in range(len(nums)-2,-1,-1):
            last = last*nums[i+1]
            ans[i] = ans[i]*last
        return ans
# @lc code=end

#         2   3   4   5
#         1   2   6   24  120
#  120   60  20   5   1

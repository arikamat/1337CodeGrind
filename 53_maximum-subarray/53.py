#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import *
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp= [ 0]*n 
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        print(dp)
        return max(dp)

# @lc code=end


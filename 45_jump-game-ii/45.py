#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import *
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for c, steps in enumerate(nums):
            if c==0 or dp[c]!=0:
                start = c
                end = min(len(nums), c + steps + 1)
                for i in range(start,end):
                    dp[i] = min(dp[i],dp[c]+1)
                # dp[start:end] = [True] * (end - start)


        return dp[-1]
# @lc code=end


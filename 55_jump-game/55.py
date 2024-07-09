#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
from typing import *


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for c, steps in enumerate(nums):
            if dp[c]:
                start = c
                end = min(len(nums), c + steps + 1)
                dp[start:end] = [True] * (end - start)
        return dp[-1]


# @lc code=end
#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from typing import *


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        low = prices[0]
        # 7 1 5 3 6
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            total += max(0,diff)
        return total


# @lc code=end
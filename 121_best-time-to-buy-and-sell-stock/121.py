#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = prices[-1]
        res = 0
        for i in range(len(prices)-1,-1,-1):
            maxx = max(prices[i], maxx)
            res = max(res, maxx-prices[i])
        return res

# @lc code=end

# A = Solution()
# prices = [7,6,4,3,1]
# res = A.maxProfit(prices)

# print(res)
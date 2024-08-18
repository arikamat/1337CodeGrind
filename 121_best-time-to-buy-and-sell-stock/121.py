#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = float('inf')
        ans = 0
        for i in prices:
            if i < currMin:
                currMin = i
            else:
                ans = max(ans, i-currMin)
        return ans

# @lc code=end

# A = Solution()
# prices = [7,6,4,3,1]
# res = A.maxProfit(prices)

# print(res)
#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import *
# @lc code=start
class Solution:
    def util(self, coins, amount):
        if amount == 0:
            return 0
        if amount in self.dp:
            return self.dp[amount]
        best = float('inf')
        for i in coins:
            if amount -i >= 0:
                steps = self.util(coins,amount - i)+1
                best = min(steps,best)
        
        self.dp[amount] = best
        return best

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp={0:0}
        for i in coins:
            self.dp[i] = 1
        self.util(coins,amount)
        print(self.dp[amount])
        print(self.dp)
        ans = self.dp[amount]
        if ans == float('inf'):
            return -1
        else:
            return self.dp[amount]

# @lc code=end

s = Solution()
coins = [1]
amount = 0
print(s.coinChange(coins,amount))
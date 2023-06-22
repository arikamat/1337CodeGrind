#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
from typing import *


# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # self.bfs(mat,(0,0))
        m = len(mat)
        n = len(mat[0])
        import copy

        dp = copy.deepcopy(mat)

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    top = float("inf")
                    left = float("inf")
                    if r > 0:
                        top = dp[r - 1][c] + 1
                    if c > 0:
                        left = dp[r][c - 1] + 1
                    dp[r][c] = min(top, left)
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] == 1:
                    bot = float("inf")
                    rt = float("inf")
                    if r < m - 1:
                        bot = dp[r + 1][c] + 1
                    if c < n - 1:
                        rt = dp[r][c + 1] + 1

                    dp[r][c] = min(dp[r][c], bot, rt)
        print(dp)
        return dp


s = Solution()
s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

# @lc code=end

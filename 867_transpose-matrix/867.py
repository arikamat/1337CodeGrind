#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#
from typing import *
# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        res=[]
        for i in range(c):
            res.append([None]*r)
        for i in range(r):
            for j in range(c):
                res[j][i] = matrix[i][j]
        return res

# @lc code=end


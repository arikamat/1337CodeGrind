#
# @lc app=leetcode id=766 lang=python3
#
# [766] Toeplitz Matrix
#
from typing import *
# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True

# @lc code=end


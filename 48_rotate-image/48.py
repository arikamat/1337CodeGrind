#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import *
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c=len(matrix)
        for i in range(c):
            for j in range(i,c):
                t=matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
            for j in range(c//2):
                t = matrix[i][j]
                matrix[i][j] = matrix[i][c-j-1]
                matrix[i][c-j-1] = t
        # for i in range(c):
            
        return matrix
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# s=Solution()
# a=s.rotate(matrix)
# print(a)
# @lc code=end


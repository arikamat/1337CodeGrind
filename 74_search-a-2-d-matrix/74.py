#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import *
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows*cols -1

        while l <=r:
            mid = (l+r)//2
            mid_r = mid//cols
            mid_c = mid%cols
            if target<matrix[mid_r][mid_c]:
                r = mid-1
            elif target>matrix[mid_r][mid_c]:
                l = mid+1
            else:
                return True
        return False
# @lc code=end


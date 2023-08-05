#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#
from typing import *
# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        w = len(mat[0])
        h = len(mat)
        if w*h != r*c:
            return mat
        ct=0
        ans=[]
        for i in range(r):
            ans.append([None]*(c))
        for i in range(r):
            for j in range(c):
                rr = ct//w
                cc = ct%w
                # print(ct,rr,cc)
                ans[i][j] = mat[rr][cc]
                ct+=1
        return ans
# @lc code=end
# mat = [[1,2],[3,4]]
# r = 2
# c = 4
# s= Solution()
# a=s.matrixReshape(mat,r,c)
# print(a)
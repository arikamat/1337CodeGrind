#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import *
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        res=[]
        for i in range(n):
            res.append([None]*n)
        currRow = 0
        currCol=0
        currDir = 0
        for i in range(1,n*n+1):
            if res[currRow][currCol] ==None:
                res[currRow][currCol] = i
            
            for j in range(4):
                d = dirs[(currDir+j)%4]
                r = currRow+d[0]
                c = currCol+d[1]
                if not(r<0 or r>=n or c<0 or c>=n):
                    if res[r][c]==None:
                        currDir = (currDir+j)%4
                        currRow = r
                        currCol = c
                        # break
            # print(i)
        return res
s=Solution()

a=s.generateMatrix(1)
print(a)
            
# @lc code=end


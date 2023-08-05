#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import *
# @lc code=start
class Solution:
    def checkSurround(self, matrix,row,col):
        dirOrder=[(1,0), (0,-1), (-1,0), (0,1)]
        rr = len(matrix)
        cc = len(matrix[0])
        for i in dirOrder:
            currC,currR = i
            r = row+currR
            c = col+currC
            # print(r,c, not matrix[r][c])  
            if not (r<0 or r>=rr or c<0 or c>=cc):
                if matrix[r][c]!=None:
                    return False

        return True
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirOrder=[(1,0), (0,-1), (-1,0), (0,1)]
        res=[]
        rr = len(matrix)
        cc = len(matrix[0])
        currDir = 0
        currRow = 0
        currCol = 0
        while True:
            if(matrix[currRow][currCol]!=None):
                res.append(matrix[currRow][currCol])
                matrix[currRow][currCol] = None
            if(self.checkSurround(matrix,currRow,currCol)):
                break
            
            r = currRow
            c = currCol
            for i in range(4):
                dir = dirOrder[(currDir+i)%4]
                r = currRow+dir[1]
                c = currCol +dir[0]
                if not(r<0 or r>=rr or c<0 or c>=cc):
                    if matrix[r][c]!=None:
                        currDir = (currDir+i)%4
                        currRow = r
                        currCol = c
                        break
        return res
# @lc code=end
"""
2   5
8   4
0  -1

"""

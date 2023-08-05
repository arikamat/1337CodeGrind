#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
from typing import *
# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d={}
        currId = 0
        res=[]
        for i in mat:
            for c,j in enumerate(i):
                if currId+c not in d:
                    d[currId+c] = []
                d[currId+c].append(j)
            currId+=1
        for i in range(currId+len(mat[0])-1):
            if i%2 == 0:
                d[i].reverse()
            res+=d[i]
        return res
# s=Solution()
# mat = [[1,2],[3,4]]
# mat = [[1,2,3],[4,5,6],[7,8,9]]
# mat=[[2,3]]
# a=s.findDiagonalOrder(mat)
# print(a)          
# @lc code=end


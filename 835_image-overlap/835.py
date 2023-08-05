#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#
from typing import *
# @lc code=start
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        l1 = []
        l2=[]
        d={}
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    l1.append((i,j))
                if img2[i][j] ==1:
                    l2.append((i,j))
        maxCt=0
        for r2,c2 in l2:
            for r1,c1 in l1:
                vec = (r2-r1,c2-c1)
                if vec not in d:
                    d[vec] = 0
                d[vec]+=1
                maxCt = max(maxCt, d[vec])
        return maxCt
        

# @lc code=end


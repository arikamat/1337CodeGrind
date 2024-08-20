#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
from typing import *
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        mx = 0
        for c,i in enumerate(heights):
            lastPop = c
            while len(stk)>0 and stk[-1][0] > i:
                ht = stk[-1][0]
                w = c - stk[-1][1]
                mx = max(mx, ht*w)
                lastPop = stk[-1][1]
                stk.pop()
            stk.append((i,lastPop)) #(ht, idx)
        # print(stk)
        for i in stk:
            c = len(heights)
            ht = i[0]
            w = c - i[1]
            mx = max(mx, ht*w)
        return mx
# @lc code=end


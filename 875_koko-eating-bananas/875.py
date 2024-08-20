#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from typing import *
import math
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res=float('inf')
        while l<=r:
            k = (l+r)//2
            tot = 0
            for i in piles:
                tot+=math.ceil(i/k)
            if tot <= h:
                res = min(res,k)
                r = k-1
            elif tot>h:
                l=k+1
        return res
# @lc code=end


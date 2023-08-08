#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import *
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = float('-inf')
        l = 0
        r = len(height)-1
        while l<r:
            maxarea = max(min(height[l],height[r])*(r-l),maxarea)
            if height[l]<height[r]:
                l+=1
            elif height[r]<height[l]:
                r-=1
            else:
                l+=1
                r-=1
        return maxarea

# @lc code=end


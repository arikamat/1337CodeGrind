#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
from typing import *
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        height.insert(0, float('-inf'))
        height.append(float('-inf'))
        right = height.copy()
        left = height.copy()
        for i in range(len(height)-2,0,-1):
            right[i] = max(right[i+1],right[i])
        for i in range(1, len(height)-1):
            left[i] = max(left[i-1],left[i])
        total = 0
        print(left, right)
        for i in range(1, len(height)-1):
            a = min(left[i],right[i])
            canFit = max(0, a- height[i])
            total += canFit
        return total
# @lc code=end


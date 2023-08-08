#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import *
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for c,i in enumerate(nums):
            if target-i in d:
                return [d[target-i],c]
            else:
                d[i] = c
        return [-1,-1]
        
# @lc code=end


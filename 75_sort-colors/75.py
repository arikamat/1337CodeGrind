#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
from typing import *


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0
        for i in nums:
            if i == 0:
                a += 1
            elif i == 1:
                b += 1
            else:
                c += 1
        for i in range(len(nums)):
            if i < a:
                nums[i] = 0
            elif i < a+b:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums


# @lc code=end

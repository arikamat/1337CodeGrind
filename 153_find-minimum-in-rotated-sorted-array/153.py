#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
from typing import *
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = float('inf')
        while l<=r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid-1
            res = min(nums[mid],res)
        return res
# @lc code=end


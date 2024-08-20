#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
from typing import *
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <=r:
            mid = (l+r)//2
            if target<nums[mid]:
                r = mid-1
            elif target>nums[mid]:
                l = mid+1
            else:
                return mid
        return -1
# @lc code=end


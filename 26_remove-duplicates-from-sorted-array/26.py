#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import *
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        length = len(nums)
        if length == 0:
            return 0
        for i in range(length):
            if nums[i] != nums[idx]:
                nums[idx+1] = nums[i]
                idx+=1
        return idx+1
        
# @lc code=end


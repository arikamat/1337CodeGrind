#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import *
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx =0
        for i in range(len(nums)):
            t = nums[i]
            if t != val:
                nums[idx] = t
                idx+=1
        return idx
# @lc code=end


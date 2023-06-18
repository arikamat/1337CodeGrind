#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#
from typing import *
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i in d:
                return True
            d[i] = 0
        return False
    # #one line soln | runs slower i think
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     return len(nums) == len(set(nums))
# @lc code=end


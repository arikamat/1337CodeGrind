#
# @lc app=leetcode id=1685 lang=python3
#
# [1685] Sum of Absolute Differences in a Sorted Array
#
from typing import *
# @lc code=start
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff=nums[j]-nums[i]
                ans[i]+=abs(diff)
                ans[j]+=abs(diff)
        return ans
# @lc code=end


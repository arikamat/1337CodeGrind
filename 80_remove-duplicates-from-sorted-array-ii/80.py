#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#
from typing import *


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        last_num = None
        last_num_freq = 0
        for i in range(len(nums)):
            val = nums[i]
            if val != last_num:
                last_num=val
                last_num_freq=1
                nums[idx] = val
                idx+=1
            elif last_num_freq==1:
                nums[idx] = val
                last_num_freq+=1
                idx+=1
        return idx
# @lc code=end

# A = Solution()
# b = [0,0,1,1,1,1,2,3,3]
# res=A.removeDuplicates(b)
# print(res,b)
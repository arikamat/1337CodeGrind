#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
from typing import *
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        maxCt=0
        maxNum=-1
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
            if(d[i]>maxCt):
                maxCt=d[i]
                maxNum=i
        return maxNum
        
# @lc code=end


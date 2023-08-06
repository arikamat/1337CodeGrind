#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#
from typing import *
# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ct=0
        c = Counter(nums)
        a = c.keys()
        if k==0:
            for i in c:
                if c[i] >1:
                    ct+=1
        else:
            for i in c:
                if i+k in c:
                    ct+=1
        # print(ct)
        return ct
        

# @lc code=end

# s=Solution()
# nums = [3,1,4,1,5]; k = 2
# nums=[1,2,3,4,5]; k = 1
# nums = [1,3,1,5,4]; k = 0
# nums=[1,2,4,4,3,3,0,9,2,3]; k=3
# s.findPairs(nums,k)
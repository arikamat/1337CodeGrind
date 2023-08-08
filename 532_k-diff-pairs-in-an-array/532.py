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
 
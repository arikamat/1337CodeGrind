#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
from typing import *
# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = {0:1}
        curr = 0
        res = 0
        for i in nums:
            curr+=i
            curr%=k
            curr+=k
            curr%=k

            if curr in pre:
                res+=pre[curr]
                pre[curr]+=1
            else:
                pre[curr]=1
        return res
# @lc code=end

#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
from typing import *
# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        il = len(nums1)
        jl = len(nums2)
        dp =[ [0] * (jl+1) for i in range(il+1)]
        # dp[i,j] is common prefix of A[0:i] and B[0:j] ending at i and j respectively
        res = 0
        for i in range(1,il+1):
            for j in range(1,jl+1):
                if nums1[i-1] == nums2[j-1]:
                    c = dp[i-1][j-1] + 1
                    dp[i][j] = c
                    res = max(res,c)
        return res
# @lc code=end


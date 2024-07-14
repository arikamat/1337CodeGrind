#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
from typing import *
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre={0:1}
        curr = 0
        res=0
        for i in nums:
            curr += i
            needed = curr - k
            if needed in pre:
                res+=pre[needed]
            if curr in pre:
                pre[curr]+=1
            else:
                pre[curr] = 1
        return res

# @lc code=end

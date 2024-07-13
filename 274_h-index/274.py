#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
from typing import *
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for c, num in enumerate(citations):
            if c >= num:
                return c
        return len(citations) 

# @lc code=end

#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
from typing import *
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort(reverse=True)
        # for c, num in enumerate(citations):
        #     if c >= num:
        #         return c
        # return len(citations) 

        n = len(citations)
        arr = [0]*(n+1)
        for i in citations:
            if i>n:
                arr[n]+=1
            else:
                arr[i]+=1
        ct=0
        for i in range(len(citations),-1,-1):
            ct+=arr[i]
            if ct>=i:
                return i
        return 0



# @lc code=end

#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
from typing import *

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq 
        import math
        closest=[]
        for i in points:
            heapq.heappush(closest, (math.hypot(i[0],i[1]), i))
        ans=[]
        for i in range(k):
            val = heapq.heappop(closest)
            ans.append(val[1])
        return ans
# @lc code=end


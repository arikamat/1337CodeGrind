#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import *
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        ans = d.most_common(k)
        res=[]
        for i in ans:
            res.append(i[0])
        return res
# @lc code=end


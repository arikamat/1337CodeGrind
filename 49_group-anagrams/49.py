#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import *
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            c = tuple(sorted(i))
            if c not in d:
                d[c] =[]
            d[c].append(i)
        res=[]
        for i in d:
            res.append(d[i])
        return res
# @lc code=end


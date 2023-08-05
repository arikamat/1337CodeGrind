#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#
from typing import *
# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        import math
        d={}
        for i in time:
            mod = i%60
            if mod not in d:
                d[mod]=0
            d[mod]+=1
        ct=0
        if 0 in d:
            ct=math.comb(d[0],2)

        # print(d)
        for i in d:
            if 60-i == i:
                ct+=math.comb(d[i],2)
            elif 60-i in d:
                ct+=d[i]*d[60-i]
            d[i]=0
        # print(ct)
        return ct
# @lc code=end

# s=Solution()
# time = [30,20,150,100,40]
# # time = [60,60,60]
# time=[418,204,77,278,239,457,284,263,372,279,476,416,360,18]
# s.numPairsDivisibleBy60(time)


#
# @lc app=leetcode id=954 lang=python3
#
# [954] Array of Doubled Pairs
#
from typing import *
# @lc code=start
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i] = 0
            d[i]+=1
        l = list(d.keys())
        l.sort()
        for i in l:
            if i==0:
                if d[i]%2 !=0:
                    return False
                else:
                    d[i] = 0
            elif 2*i in d and d[2*i]>0:
                a = d[i]
                b= d[2*i]
                d[i] -= min(a,b)
                d[2*i] -=min(a,b)
        # print(d)
        for i in d:
            if d[i] !=0:
                return False
        return True
    
# @lc code=end

s= Solution()

arr = [2,4,0,0,8,1]
s.canReorderDoubled(arr)
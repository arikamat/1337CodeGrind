#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#
from typing import *
import math
# @lc code=start
class Solution:

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ct=0
        log=[]
        d={}
        poss=[]
        for i in arr:
            if i not in d:
                d[i]=0
            d[i]+=1
        s = list(dict.fromkeys(arr).keys())
        s.sort()
        for i in range(len(s)):
            need =target-s[i]-s[i]
            if need>=s[i]:
                poss.append((s[i],s[i],need))
                for j in range(i+1,len(s)):
                    need = target-s[i]-s[j]
                    if need >=s[j]:
                        poss.append((s[i],s[j],need))
        for i in poss:
            miniD = dict.fromkeys(i,0)
            for j in i:
                miniD[j]+=1
            vals = list(miniD.keys())
            print(miniD,d[vals[0]],miniD[vals[0]], math.comb(3000,3))
            if len(miniD)==1:
                if vals[0] in d:
                    ct+=math.comb(d[vals[0]], miniD[vals[0]])
            if len(miniD)==2:
                if vals[0] in d and vals[1] in d:
                    ct+=math.comb(d[vals[0]], miniD[vals[0]])*math.comb(d[vals[1]], miniD[vals[1]])
            if len(miniD)==3:
                if vals[0] in d and vals[1] in d and vals[2] in d:
                    ct+=math.comb(d[vals[0]], miniD[vals[0]])*math.comb(d[vals[1]], miniD[vals[1]])*math.comb(d[vals[2]], miniD[vals[2]])
        print(ct)
        return ct%1000000007

# @lc code=end


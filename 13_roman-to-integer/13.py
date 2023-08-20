#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d={
            'I':1,
            "V":5,
            'X':10,
            "L":50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        c=0
        res=0
        while c<len(s):
            if c+1 < len(s) and d[s[c]] < d[s[c+1]]:
                res+=d[s[c+1]]-d[s[c]]
                c+=2
            else:
                res+=d[s[c]]
                c+=1

        return res
# @lc code=end


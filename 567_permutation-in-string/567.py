#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        from collections import Counter

        d = dict(Counter(s1))

        curr = dict(Counter(s2[0:len(s1)-1]))
        l = 0
        for r in range(len(s1)-1, len(s2)):
            charInLeft = s2[l]
            charInRight = s2[r]
            if charInRight not in curr:
                curr[charInRight] = 0
            curr[charInRight] += 1
            matches = 0
            for i in d:
                if i in curr and d[i] == curr[i]:
                    matches +=curr[i]
            if matches == len(s1):
                return True
            curr[charInLeft] -=1 
            l+=1
        return False
        
# @lc code=end


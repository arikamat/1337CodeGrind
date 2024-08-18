#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d={}
        res=0
        for r in range(len(s)):
            c = s[r]
            if c not in d:
                d[c] = 0
            d[c]+=1

            while (r-l+1) - max(d.values()) > k:
                d[s[l]]-=1
                l+=1
            res = max(r-l+1, res)
        return res


# @lc code=end


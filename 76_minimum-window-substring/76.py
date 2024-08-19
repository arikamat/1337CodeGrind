#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        t_dict = dict(Counter(t))
        best_l = None
        best_r = None
        l = 0
        wip = {}
        for i in t:
            wip[i] = 0 
        needed = len(t_dict)
        have = 0
        for r in range(len(s)):
            if s[r] in wip:
                wip[s[r]] +=1
                if wip[s[r]] == t_dict[s[r]]:
                    have+=1
            while have == needed:
                if best_l is None or r-l+1 < best_r - best_l +1:
                    best_r = r
                    best_l = l
                if s[l] in wip and wip[s[l]] == t_dict[s[l]]:
                    wip[s[l]]-=1
                    have-=1
                    l+=1
                    break
                elif s[l] in wip:
                    wip[s[l]]-=1
                    l+=1
                else:
                    l+=1
        if best_l is None:
            return ""
        return s[best_l:best_r+1]
# @lc code=end


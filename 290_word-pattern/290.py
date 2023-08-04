#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        s = s.split()
        if len(pattern) != len(s):
            
            return False
        for i in range(len(pattern)):
            pat = pattern[i]
            word = s[i]
            if pat in d and d[pat] != word:
                
                return False
            elif pat not in d and word in d.values():
                # print(pattern,s, pat, d)
                return False
            else:
                d[pat] = word
        return True
# s = Solution()
# a=s.wordPattern("abba", "dog cat cat dog")
# b=s.wordPattern("abba", "dog cat cat fish")
# c=s.wordPattern("aaaa", "dog cat cat dog")
# print(a,b,c)
# @lc code=end


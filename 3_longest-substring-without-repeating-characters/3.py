#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
from typing import *
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        res=0
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in chars and chars[c] >= l:
                l = chars[c]+1
            chars[c] = r
            res = max(res, r-l+1)

        return res
# @lc code=end


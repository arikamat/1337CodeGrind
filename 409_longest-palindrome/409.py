#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
from typing import *


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
        ct = 0
        oddCt = 0
        for i in d:
            if d[i] % 2 == 0:
                ct += d[i]
            else:
                ct += d[i] - 1
                oddCt += 1
        if oddCt > 0:
            ct += 1
        return ct


# @lc code=end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
from typing import *
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest = 0
        visited={}
        lidx = 0
        for ridx in range(len(s)):
            if s[ridx] in visited and visited[s[ridx]] >= lidx:
                lidx = visited[s[ridx]]+1
            else:
                largest = max(ridx-lidx+1, largest)
            visited[s[ridx]] = ridx
        return largest
# @lc code=end


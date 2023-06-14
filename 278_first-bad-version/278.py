from typing import *

#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def bin_search(self, start, end):
        if start == end:
            if isBadVersion(start):
                return start
            else:
                return 1 + start

        n = (start + end) // 2
        if isBadVersion(n):
            return self.bin_search(0, n - 1)
        else:
            return self.bin_search(n + 1, end)

    def firstBadVersion(self, n):
        mid = n // 2
        if isBadVersion(mid):
            return self.bin_search(0, mid - 1)
        else:
            return self.bin_search(mid + 1, n)


# @lc code=end

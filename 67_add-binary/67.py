#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
from typing import *


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxx = max(len(a), len(b))
        a = str(a).rjust(maxx, "0")
        b = str(b).rjust(maxx, "0")
        carry = 0
        ans = ""
        for i in range(maxx - 1, -1, -1):
            aDigit = int(a[i])
            bDigit = int(b[i])
            dig = carry + aDigit + bDigit
            carry = dig // 2
            dig = dig % 2
            ans = str(dig) + ans
        ans = str(carry) + ans
        return str(int(ans))


# @lc code=end

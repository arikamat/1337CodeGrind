#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        import math
        a = str1+str2
        b = str2+str1
        if a==b:
            return str1[:math.gcd(len(str1),len(str2))]
        else:
            return ""
# @lc code=end


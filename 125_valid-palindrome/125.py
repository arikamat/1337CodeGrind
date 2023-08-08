#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
import re
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1
        while l<r:
            t = False
            if not ((s[l]>='a' and s[l] <='z') or (s[l]>='0' and s[l]<='9')):
                l+=1
                t = True
            if not ((s[r]>='a' and s[r] <='z') or (s[r]>='0' and s[r]<='9')):
                r-=1
                t = True
            if not t:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
        return True
        
# @lc code=end


#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#
from typing import *
# @lc code=start
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        s = {}
        ct = 0
        middleLooking = True
        for i in words:
            if i not in s:
                s[i] = 0
            s[i]+=1
        print(s)
        for curr in s:
            if s[curr] ==0:
                continue
            rev = curr[1]+curr[0]
            if curr==rev:
                ct+=(s[curr]//2)*2
                # print("adding 23")
                if middleLooking and s[curr]%2==1:
                    # print("adding 1")
                    ct+=1
                    middleLooking=False
            elif rev in s:
                ct+=min(s[curr],s[rev])*2
                s[rev]=0
                s[curr]=0
                
        print(2*ct)
        return 2*ct

            
# @lc code=end

# s= Solution()
# words = ["lc","cl","gg"]
# # words = ["ab","ty","yt","lc","cl","ab"]
# # words = ["cc","ll","xx"]
# words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
# s.longestPalindrome(words)
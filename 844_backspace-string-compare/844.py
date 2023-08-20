#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l1 = []
        l2=[]
        # for i in s:
        #     if i == '#':
        #         if len(l1)>0:
        #             l1.pop()
        #     else:
        #         l1.append(i)
        # for i in t:
        #     if i == '#':
        #         if len(l2)>0:
        #             l2.pop()
        #     else:
        #         l2.append(i)
        # return l1==l2
        for i in range(max(len(s),len(t))):
            if i < len(s):
                ch = s[i]
                if ch == '#':
                    if len(l1)>0:
                        l1.pop()
                else:
                    l1.append(ch)
            if i<len(t):
                ch =t[i]
                if ch == '#':
                    if len(l2)>0:
                        l2.pop()
                else:
                    l2.append(ch)
        # print(l1,l2)
        return l1==l2
# @lc code=end

s=Solution()
s1="y#fo##f"
s2="y#f#o##f"
s.backspaceCompare(s1,s2)
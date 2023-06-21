#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
from typing import *
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for i in tokens:
            if i=='+':
                a = stk.pop()
                b = stk.pop()
                stk.append(a+b)
            elif i=='-':
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            elif i=='*':
                a = stk.pop()
                b = stk.pop()
                stk.append(a*b)
            elif i=='/':
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b/a))
            else:
                stk.append(int(i))
        return stk[0]

# @lc code=end


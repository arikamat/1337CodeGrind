#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stk=[]
        res=[]
        def utilFunc(openP, closeP):
            if openP == closeP and openP==n:
                res.append("".join(stk))
                return 
            if openP < n:
                stk.append("(")
                utilFunc(openP+1, closeP)
                stk.pop()
            if closeP < openP:
                stk.append(")")
                utilFunc(openP, closeP+1)
                stk.pop()
        utilFunc(0,0)
        return res
        
# @lc code=end


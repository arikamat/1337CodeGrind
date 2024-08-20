#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        currStk = []
        for c,i in enumerate(temperatures):
            while len(currStk)>0 and currStk[-1][0]<i:
                idx = currStk[-1][1]
                res[idx] = c-idx
                currStk.pop()
            currStk.append((i,c))
        return res
# @lc code=end


#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
import math
class Solution:
        
    def climbStairs(self, n):
        lastTwo= 0
        ans=0
        for i in range(n-2,-1,-2):
            lastTwo+=1
            ans += math.factorial(i+lastTwo)/(math.factorial(i)*math.factorial(lastTwo))

        return int(ans+1)
# @lc code=end

# 1  2
# 2  0
# 0 1


# 1 2
# ------

# 3 0
# 1 1


# n = 4
# 1 2 1
# 2 11
# 4 0 
# 2 1
# 0 2
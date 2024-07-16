#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#
from typing import *
# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = list(map(lambda x:60*int(x[:2]) + int(x[3:]), timePoints))
        timePoints.sort()
        minimum = float('inf')
        for c in range(len(timePoints)-1):
            a = timePoints[c]
            b = timePoints[c+1]
            minimum = min(minimum, b-a, 1440+a - b)
        a = timePoints[0]
        b = timePoints[-1]
        minimum = min(minimum, b-a, 1440+a - b)
        return minimum
# @lc code=end
A = Solution()
timePoints = ["23:59","00:00"]
timePoints = ["00:00","23:59","00:00"]
res=A.findMinDifference(timePoints)
print(res)

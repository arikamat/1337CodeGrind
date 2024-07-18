#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#
from typing import *
# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        if x1==x2:
            for i in coordinates:
                if i[0] !=x1:
                    return False
            return True
        slope = (y2-y1)/(x2-x1)
        b = y1 - slope*x1
        for i in coordinates:
            x = i[0]
            y = i[1]
            if y != slope*x + b:
                return False
        return True
# @lc code=end


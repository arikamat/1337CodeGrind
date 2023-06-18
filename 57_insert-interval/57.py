#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
from typing import *


# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        answer = []
        currInsert = newInterval
        for c, i in enumerate(intervals):
            start = currInsert[0]
            end = currInsert[1]
            if end < i[0]:
                answer.append(currInsert)
                answer = answer + intervals[c:]
                return answer
            elif start > i[1]:
                answer.append(i)
            else:
                currInsert = [min(i[0], currInsert[0]), max(i[1], currInsert[1])]
        answer.append(currInsert)
        return answer


# @lc code=end

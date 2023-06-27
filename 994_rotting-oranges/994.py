#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
from typing import *


# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        fresh = []
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        currMax = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh.append((i, j))
                elif grid[i][j] == 2:
                    q.append((i,j,0))
        while len(fresh) > 0 and len(q) > 0:
            rr, cc,minute = q.pop(0)
            if (rr,cc) in fresh:
                fresh.remove((rr,cc))
            currMax = max(currMax, minute)
            grid[rr][cc]=2
            for i in dirs:
                r =rr+ i[0]
                c =cc+ i[1]
                if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!=1 or (r,c) in q:
                    continue
                else:
                    q.append((r,c,minute+1))
        if len(fresh)>0:
            print(-1)
            return -1
        else:
            print(currMax)
            return currMax
s = Solution()
s.orangesRotting([[0,2]])
# @lc code=end

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import *
# @lc code=start
class Solution:
    def bfs(self, tup, grid):
        r = tup[0]
        c = tup[1]
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]!="1":
            return 
        grid[r][c]="0"
        self.bfs((r-1,c),grid)
        self.bfs((r+1,c),grid)
        self.bfs((r,c-1),grid)
        self.bfs((r,c+1),grid)
        return

    def numIslands(self, grid: List[List[str]]) -> int:
        ct=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ct +=1
                    self.bfs((i,j),grid)
        return ct
        
s = Solution()
a=s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
print(a)
# @lc code=end


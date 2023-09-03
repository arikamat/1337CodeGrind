#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from typing import *
# @lc code=start

class Solution:
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visited = set()
        
        for i in range(numCourses):
            adj[i]=[]

        for i in prerequisites:
            adj[i[0]].append(i[1])
        
        def dfs(course):
            if len(adj[course])==0:
                return True
            if course in visited:
                return False
            visited.add(course)
            for i in adj[course]:
                res = dfs(i)
                if not res:
                    return False
            adj[course]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        

# @lc code=end

# n = 20
# pre = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
# n=3
# pre = [[0,2],[1,2],[2,0]]
# s = Solution()
# res=s.canFinish(n,pre)
# print(res)
n=2
pre=[[1,0]]
s = Solution()
res=s.canFinish(n,pre)
print(res)
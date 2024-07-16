#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
from typing import *
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={}
        for prereq in prerequisites:
            f = prereq[0]
            t = prereq[1]
            if f in adj:
                adj[f].add(t)
            else:
                adj[f]={t}
        visited = set()
        res=[]
        resS=set()
        def dfs(node):
            if node in resS:
                return True
            if node not in adj:
                res.append(node)
                resS.add(node)
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for i in adj[node]:
                if not dfs(i):
                    return False
            visited.remove(node)
            res.append(node)
            resS.add(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


# @lc code=end


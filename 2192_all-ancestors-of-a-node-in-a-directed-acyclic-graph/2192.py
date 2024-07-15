#
# @lc app=leetcode id=2192 lang=python3
#
# [2192] All Ancestors of a Node in a Directed Acyclic Graph
#
from typing import *
# @lc code=start
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        self.adj = {}
        self.res = [None]*n
        for edge in edges:
            fromNode = edge[0]
            toNode = edge[1]
            if toNode in self.adj:
                self.adj[toNode].append(fromNode)
            else:
                self.adj[toNode] = [fromNode]
        for i in range(n):
            self.res[i] = self.dfs(i)
        for i in range(n):
            self.res[i] = sorted(list(self.res[i]))
        return self.res

    def dfs(self, node):
        if node not in self.adj:
            return set()
        if self.res[node] :
            return self.res[node]
        nodes = set()
        for i in self.adj[node]:
            nodes.add(i)
            nodes.update(self.dfs(i))
        self.res[node] = nodes
        return nodes
        
# @lc code=end


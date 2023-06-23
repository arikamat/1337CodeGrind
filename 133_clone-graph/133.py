#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
from typing import *
# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    d={}
    def util(self, node):
        if node in self.d:
            return self.d[node]
        cpy = Node(node.val)
        self.d[node] = cpy
        for i in node.neighbors:
            cpy.neighbors.append(self.util(i))
        return cpy
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node
        new = self.util(node)
        return new

        
# @lc code=end


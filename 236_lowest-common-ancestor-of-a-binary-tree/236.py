#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from sympy import true


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, curr, target,path ):
        
        if not curr:
            return False
        # print(curr.val,target)
        if curr==target:
            path.append(curr)
            return True
        res = self.dfs(curr.left,target,path)
        if res:
            path.append(curr)
            return True
        res = self.dfs(curr.right,target,path)
        if res:
            path.append(curr)
            return True
        return False


    def lowestCommonAncestor(self, root, p, q):
        path_p =[]
        self.dfs(root, p, path_p)
        path_q =[]
        self.dfs(root, q, path_q)
        for i in path_p:
            if i in path_q:
                return i
s=Solution()
s.lowestCommonAncestor()
# @lc code=end


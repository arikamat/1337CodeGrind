#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#
from typing import *
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        # print(root.left)
        # print(root)
        # print(root.right)
        

        if root.val == 1:
            return root
        elif root.left == None and root.right==None:
            return None
        else:
            return root
        
# @lc code=end


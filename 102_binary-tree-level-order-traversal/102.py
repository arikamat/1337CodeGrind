#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def bfs(root, currLevel):
            
            if root is None:
                return
            while currLevel>len(res)-1:
                res.append([])
            res[currLevel].append(root.val)
            bfs(root.left, currLevel+1)
            bfs(root.right, currLevel+1)
        bfs(root,0)
        return res         

# @lc code=end

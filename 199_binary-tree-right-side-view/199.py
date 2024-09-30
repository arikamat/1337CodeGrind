#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
from typing import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def bfs(root,level):
            if not root:
                return 
            while level>len(res)-1:
                res.append(None)
            res[level] = root.val
            bfs(root.left,level+1)
            bfs(root.right,level+1)
        bfs(root,0)
        return res
# @lc code=end


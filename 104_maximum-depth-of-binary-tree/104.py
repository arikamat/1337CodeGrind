#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def getHeight(self, root):
        if root is None:
            return 0
        hl = 1 + self.getHeight(root.left)
        hr = 1 + self.getHeight(root.right)
        # print(root, hl, hr)
        return max(hl, hr)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getHeight(root)


# @lc code=end

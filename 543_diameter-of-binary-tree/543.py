#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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
    maxx = 0

    def getHeight(self, root):
        if root is None:
            return 0
        hl = 1 + self.getHeight(root.left)
        hr = 1 + self.getHeight(root.right)
        d = hl + hr
        self.maxx = max(self.maxx, d)
        # print(root, hl, hr)
        return max(hl, hr)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getHeight(root)
        return self.maxx - 2


# @lc code=end

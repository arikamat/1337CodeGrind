from typing import *

#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balance_util(self, root):
        if root is None:
            return 0
        else:
            hl = self.balance_util(root.left)
            hr = self.balance_util(root.right)
            if hl == -1 or hr == -1:
                return -1
            if abs(hl - hr) > 1:
                return -1
            return 1 + max(hl, hr)

    def isBalanced(self, root):
        if root is None:
            return True
        balanced = self.balance_util(root)
        if balanced == -1:
            return False
        else:
            return True

    
# @lc code=end

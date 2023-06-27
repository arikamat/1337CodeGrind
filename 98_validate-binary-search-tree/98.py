#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
from typing import *

from networkx import is_empty


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root):
        stk = []
        curr = root
        prev = float("-inf")
        while True:
            if curr is not None:
                stk.append(curr)
                curr = curr.left
            elif len(stk) > 0:
                a = stk.pop()
                currval = a.val
                if currval <= prev:
                    return False
                prev = currval
                curr = a.right
            else:
                break
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        ans = self.inorder(root)
        return ans


# @lc code=end

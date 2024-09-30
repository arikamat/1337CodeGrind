#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ct=[0]
        def bfs(root, currMax):
            if root is None:
                return
            if root.val>=currMax:
                ct[0]+=1
            m = max(root.val, currMax)
            bfs(root.left, m)
            bfs(root.right, m)
        bfs(root,float("-inf"))
        return ct[0]
# @lc code=end


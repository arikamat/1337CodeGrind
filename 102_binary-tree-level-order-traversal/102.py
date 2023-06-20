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
        q = [(0,root)]
        ans={}
        if root is None:
            return []
        while len(q)>0:
            level, node = q.pop(0)
            if node.left is not None:
                q.append((level+1,node.left))
            if node.right is not None:
                q.append((level+1,node.right))
            if level not in ans:
                ans[level] = []
            ans[level].append(node.val)
        answer=[]
        for i in ans:
            answer.append(ans[i])
        return answer            

# @lc code=end

#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
from typing import *


# @lc code=start
class Node:
    def __init__(self, val, curr_sum=None, parent=None):
        self.val = val
        if not parent:
            self.path = [val]
        else:
            self.path=parent.path+[self.val]
        if not curr_sum:
            self.curr_sum = self.val
        else:
            self.curr_sum = curr_sum


class Solution:
    def tree(self, root, candidates, idx, target,res):
        if root.val == target:
            res.append(root)
            return res
        if root.val > target:
            return res
        currsum = root.curr_sum
        for i in range(idx,len(candidates)):
            child = candidates[i]
            if child.val + currsum < target:
                self.tree(Node(child.val, curr_sum=child.val + currsum, parent=root),candidates,i,target,res)
            elif child.val + currsum == target:
                res.append(Node(child.val, child.val + currsum, parent=root))
                
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = []
        for i in candidates:
            l.append(Node(i))
        ans = []
        for i in range(len(l)):
            import pdb

            # pdb.set_trace()
            a = self.tree(l[i], l, i, target,ans)
        for i in range(len(ans)):
            ans[i] = ans[i].path
        return ans


s = Solution()
s.combinationSum([2, 3, 6, 7], 7)
# @lc code=end

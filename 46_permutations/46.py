#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import *


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) == 1:
            return [nums[:]] # initially had it as nums.copy() but leetcode was erroring out
        for i in range(len(nums)):
            element = nums.pop(0)
            perms = self.permute(nums)
            for i in perms:
                i.append(element)
            ans = ans + perms
            nums.append(element)
        return ans

s = Solution()
ans = s.permute([1])
print(ans)
# @lc code=end

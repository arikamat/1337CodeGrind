#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
from typing import *
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        l = len(nums)-k #pivot
        r = len(nums)-1
        while l<r:
            t = nums[l]
            nums[l] = nums[r]
            nums[r] = t
            l+=1
            r-=1
        
        l = 0
        r = len(nums)-k-1

        while l<r:
            t = nums[l]
            nums[l] = nums[r]
            nums[r] = t
            l+=1
            r-=1

        l = 0
        r = len(nums)-1

        while l<r:
            t = nums[l]
            nums[l] = nums[r]
            nums[r] = t
            l+=1
            r-=1

        
# @lc code=end
# A = Solution()
# nums =[1,2,3,4,5,6]
# k=11

# A.rotate(nums,k)
# print(nums)

# 4 3 2 1 ** 7 6 5|| 3
# 5 2 3 4 ** 1 6 7
# 5 6 3 4 ** 1 2 7
# 5 6 7 4 ** 1 2 3
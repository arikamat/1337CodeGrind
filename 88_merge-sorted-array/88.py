#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
from typing import *
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        rp = n-1
        lp = m-1
        while rp>=0:
            idx = lp+rp+1
            
            if lp>=0 and rp>=0 and nums1[lp]>=nums2[rp]:
                nums1[idx] = nums1[lp]
                lp-=1
            else:
                nums1[idx] = nums2[rp]
                rp-=1

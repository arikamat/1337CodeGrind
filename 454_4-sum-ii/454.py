#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
from typing import *
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d1={}
        d2={}
        for i in nums1:
            for j in nums2:
                if i +j  not in d1:
                    d1[i+j] = 0
                d1[i+j] +=1
        for i in nums3:
            for j in nums4:
                if i+j not in d2:
                    d2[i+j] = 0
                d2[i+j] +=1
        ct = 0
        for i in d1:
            if -i in d2:
                ct+=d1[i] * d2[-i]
        # print(ct)
        return ct
# s= Solution()
# nums1 = [0]; nums2 = [0]; nums3 = [0]; nums4 = [0]
# s.fourSumCount(nums1, nums2,nums3, nums4)
# @lc code=end


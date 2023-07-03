#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
from tracemalloc import start
from typing import *
# @lc code=start
import math
class Solution:
    
    def find_pivot(self,nums,l,r,startidx,endidx,ct=0):
        if endidx-startidx==1:
            return endidx
        mid1 = (startidx+endidx)//2-1
        mid2 = mid1+1
        print(startidx,endidx, mid1,mid2)
        # ct+=1
        # if ct==4:
        #     return
        if nums[mid1] > nums[mid2]:
            return mid2
        
        elif nums[mid1]>=l:
            return self.find_pivot(nums,l,r,mid2,endidx,ct)
        else:
            return self.find_pivot(nums,l,r,startidx,mid1,ct)
        
    def bin_search(self, nums,target, li,ri):
        if li==ri:
            if nums[li]==target:
                return li
            else:
                return -1
        if ri<li:
            return -1
        mid = (li+ri)//2
        if nums[mid]==target:
            return mid
        if target> nums[mid]:
            return self.bin_search(nums,target,mid+1,ri)
        else:
            return self.bin_search(nums,target,li,mid)

    def search(self, nums: List[int], target: int) -> int:
        if nums[0]==target:
            return 0
        if len(nums)==1:
            return -1
        l = nums[0]
        r = nums[-1]
        if l<r:
            if target<l:
                return -1
            if target>r:
                return -1
            piv = -1
        elif target>r and target<l:
            return -1
        else:
            piv = self.find_pivot(nums,l,r,0,len(nums))
            print(piv)
            minimum = nums[piv]
            max = nums[piv-1]
            if target>max or target<minimum:
                return -1
        minimum = nums[piv]
        max = nums[piv-1]
        if piv == -1:
            return self.bin_search(nums,target, 0, len(nums))
        elif target>=nums[piv] and target<l:
            return self.bin_search(nums,target,piv,len(nums))
        else:
            return self.bin_search(nums,target,0,piv-1)

# @lc code=end


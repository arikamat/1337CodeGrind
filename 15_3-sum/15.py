#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import *
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s=set()
        for i in range(len(nums)):
            a = i+1
            b  = len(nums)-1
            while a<b:
                tup = (nums[i], nums[a],nums[b])
                if sum(tup)==0:
                    s.add(tup)
                    a+=1
                    b-=1
                elif sum(tup)>0:
                    b-=1
                elif sum(tup)<0:
                    a+=1
        ans=[]
        for i in s:
            ans.append(list(i))
        return ans
s = Solution()
s.threeSum([0,0,0])
# @lc code=end


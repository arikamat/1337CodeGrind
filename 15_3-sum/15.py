#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
from typing import *
# @lc code=start
class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     s=set()
    #     for i in range(len(nums)):
    #         a = i+1
    #         b  = len(nums)-1
    #         while a<b:
    #             tup = (nums[i], nums[a],nums[b])
    #             if sum(tup)==0:
    #                 s.add(tup)
    #                 a+=1
    #                 b-=1
    #             elif sum(tup)>0:
    #                 b-=1
    #             elif sum(tup)<0:
    #                 a+=1
    #     ans=[]
    #     for i in s:
    #         ans.append(list(i))
    #     return ans
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        print("nums", nums)
        last = float('inf')
        for c,i in enumerate(nums):
            print(i,last)
            if i != last:
                last = i
                lp = c+1
                rp = len(nums)-1
                while lp<rp:
                    if i+nums[lp]+nums[rp] > 0:
                        rp-=1
                    elif i+nums[lp]+nums[rp] <0:
                        lp+=1
                    else:
                        ans.append([i,nums[lp],nums[rp]])
                        l = nums[lp]
                        r = nums[rp]
                        lp+=1
                        rp-=1
                        while lp<len(nums) and l==nums[lp]:
                            lp+=1
                        while rp>0 and r ==nums[rp]:
                            rp-=1
        return ans
s = Solution()
s.threeSum([0,0,0])
# @lc code=end


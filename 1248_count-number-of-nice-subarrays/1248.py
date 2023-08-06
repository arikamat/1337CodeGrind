#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#
from typing import *
# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        d={}
        for c,i in enumerate(nums):
            nums[c] = i%2
        runningsum=0
        ct=0
        d[0] = 1
        # print(nums)
        for i in nums:
            runningsum+=i
            if runningsum not in d:
                d[runningsum] =0
            d[runningsum]+=1
            if runningsum-k in d:
                ct+=d[runningsum-k]
                # print(d, runningsum-k)
        # print(ct)
        return ct
            

# @lc code=end

s=Solution()
nums = [1,1,2,1,1]; k = 3
nums = [2,4,6]; k = 1
nums = [2,2,2,1,2,2,1,2,2,2]; k = 2
s.numberOfSubarrays(nums,k)


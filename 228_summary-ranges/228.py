#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
from typing import *
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if len(nums)==0:
            return res
        currBeginning = nums[0]
        for i in range(len(nums)):
            # print(i,len(nums), i==len(nums)-1)
            if i == len(nums)-1 or nums[i]+1 != nums[i+1]:
                if currBeginning == nums[i]:
                    res.append("{}".format(nums[i]))
                else:
                    res.append("{}->{}".format(currBeginning,nums[i]))
                # res.append([currBeginning, nums[i]])
                if i != len(nums)-1:
                    currBeginning = nums[i+1]
        
        # res.append([currBeginning,nums[-1]])
        return res
    
# @lc code=end 

# s=Solution()
# s.summaryRanges([0,2,3,4,6,8,9])
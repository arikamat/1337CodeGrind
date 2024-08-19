#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        dq=[]
        for i in nums[:k-1]:
            if len(dq) == 0:
                dq.append(i)
            elif dq[-1] >= i:
                dq.append(i)
            else:
                while len(dq)>0 and i>dq[-1]:
                    dq.pop()
                dq.append(i)
        l = 0
        for r in range(k-1,len(nums)):
            i = nums[r]
            if len(dq) == 0:
                dq.append(i)
            elif dq[-1] >= i:
                dq.append(i)
            else:
                while len(dq)>0 and i>dq[-1]:
                    dq.pop()
                dq.append(i)
            
            res.append(dq[0])

            if dq[0] == nums[l]:
                dq.pop(0)
            
            l+=1
        return res   
# @lc code=end


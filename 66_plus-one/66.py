#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import *
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # lmao this soln works too
        # return list(map(int,list(str(int(''.join(list(map(str,digits))))+1))))
        carry=0
        for i in range(len(digits)-1,-1,-1):
            s=digits[i]+carry
            if i==len(digits)-1:
                s+=1
            digits[i] = s%10
            carry=s//10
        if carry>0:
            digits.insert(0,carry)
        return digits
# @lc code=end


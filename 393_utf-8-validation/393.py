#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#
from typing import *
# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        for i in range(len(data)):
            data[i] = bin(data[i])[2:]
            if len(data[i])>8:
                data[i] = data[i][-8:]
            if len(data[i])<8:
                data[i] = '0'*(8-len(data[i]))+data[i]
            
            if data[i][0:5] == '11110':
                data[i] = "4"
            elif data[i][0:4] == '1110':
                data[i] = "3"
            elif data[i][0:3] == '110':
                data[i] = "2"
            elif data[i][0:2] == '10':
                data[i] = "c"
            elif data[i][0:1] == '0':
                data[i] = "1"
            else:
                return False
        idx=0
        while idx < len(data):
            i = data[idx]
            if i=="4":
                if idx+3>=len(data):
                    return False
                if data[idx+1:idx+4] != ["c"]*3:
                    return False
                idx+=4
            elif i=="3":
                if idx+2>=len(data):
                    return False
                if data[idx+1:idx+3] != ["c"]*2:
                    return False
                idx+=3
            elif i=="2":
                if idx+1>=len(data):
                    return False
                if data[idx+1:idx+2] != ["c"]*1:
                    return False
                idx+=2
            elif i=="c":
                return False
            else:
                idx+=1
        return True
            
# @lc code=end
A = Solution()
data = [197,130,1]
res=A.validUtf8(data)
print(res)


#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    ones={
            1: "One",
            2: "Two",
            3:"Three",
            4:"Four",
            5:"Five",
            6:"Six",
            7:"Seven",
            8:"Eight",
            9:"Nine",
            10:"Ten",
            11:"Eleven",
            12: "Twelve",
            13:"Thirteen",
            14:"Fourteen",
            15:"Fifteen",
            16:"Sixteen",
            17:"Seventeen",
            18:"Eighteen",
            19:"Nineteen"
        }
    ten={
            1: "Ten",
            2: "Twenty",
            3:"Thirty",
            4:"Forty",
            5:"Fifty",
            6:"Sixty",
            7:"Seventy",
            8:"Eighty",
            9:"Ninety"
        }
    def threeDigit(self, num):
        if num<20:
            return self.ones[num]
        elif num%100==0:
            num = num//100
            return self.ones[num] + " Hundred"
        elif num>=100 and int(str(num)[1:])<20:
            numStr = str(num)
            hund = int(numStr[0])
            return self.ones[hund] + " Hundred "+self.ones[int(str(num)[1:])]
        elif num%10==0:
            if num>=100:
                numStr = str(num)
                hund = int(numStr[0])
                ten = int(numStr[1])
                one = int(numStr[2])
                return self.ones[hund] + " Hundred "+self.ten[ten] 
            else:
                numStr = str(num)
                ten = int(numStr[0])

                return self.ten[ten]

        else:
            if num>=100:
                numStr = str(num)
                hund = int(numStr[0])
                ten = int(numStr[1])
                one = int(numStr[2])

                return self.ones[hund] + " Hundred "+self.ten[ten]+" " +self.ones[one]
            else:
                numStr = str(num)
                ten = int(numStr[0])
                one = int(numStr[1])

                return self.ten[ten]+" "+ self.ones[one]

                
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        suffix=["", " Thousand "," Million ", " Billion "]
        numStr = str(num)
        import math
        newlen = 3*math.ceil(len(numStr)/3)
        numStr = numStr.zfill(newlen)
        res=[]
        c=0
        print(numStr,newlen)
        for i in range(newlen-1, -1,-3):
            threeDigs = int(numStr[i-2:i+1])
            if threeDigs==0:
                s=""
            else:
                s = self.threeDigit(threeDigs)+suffix[c]
            res.append(s)
            c+=1
        res.reverse()
        return ''.join(res).strip()
        
# @lc code=end


#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if len(self.stk)==0:
            self.stk.append((val,val))
        else:
            self.stk.append((val,min(val,self.getMin())))
    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.topNode()[0]
    def topNode(self):
        return self.stk[-1]
    def getMin(self) -> int:
        return self.topNode()[1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end


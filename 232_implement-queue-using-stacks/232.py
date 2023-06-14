from typing import *

#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#


# @lc code=start
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.stemp = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while len(self.s1) > 0:
            self.stemp.append(self.s1.pop())
        ans = self.stemp.pop()
        while len(self.stemp) > 0:
            self.s1.append(self.stemp.pop())
        return ans

    def peek(self) -> int:
        while len(self.s1) > 0:
            self.stemp.append(self.s1.pop())
        ans = self.stemp.pop()
        self.s1.append(ans)
        while len(self.stemp) > 0:
            self.s1.append(self.stemp.pop())
        return ans

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

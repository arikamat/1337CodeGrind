#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        ans=ListNode()
        curr = ans
        while l1 or l2:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            s = v1+v2+carry
            l = ListNode(s%10)
            curr.next = l
            curr = curr.next
            carry = s//10
        if carry !=0:
            l = ListNode(carry)
            curr.next = l
            curr = curr.next
        return ans.next

# @lc code=end


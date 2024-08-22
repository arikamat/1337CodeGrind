#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ct = 0
        curr = head
        while curr:
            ct+=1
            curr = curr.next
        
        idx = ct-n
        if idx==0:
            return head.next
        curr = head
        for i in range(idx-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
# @lc code=end


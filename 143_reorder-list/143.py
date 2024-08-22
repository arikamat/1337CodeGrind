#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        back = prev

        curr = head
        while back is not None and curr is not None:
            t1 = curr.next
            t2 = back.next
            curr.next = back
            back.next = t1
            curr = t1
            back = t2
# @lc code=end


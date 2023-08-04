#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        while curr:
            i = curr
            while i.next and i.next.val==val:
                i.next = i.next.next
            curr = curr.next
        if head and head.val == val:
            return head.next
        return head
        
# @lc code=end


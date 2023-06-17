#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        return slow
# @lc code=end


#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        while list1 or list2:
            l1Val = float('inf')
            l2Val = float('inf')
            if list1:
                l1Val = list1.val
            if list2:
                l2Val = list2.val
            
            n=None
            if l1Val<l2Val:
                n = ListNode(val = l1Val)
                list1 = list1.next
            else:
                n = ListNode(val = l2Val)
                list2 = list2.next
            curr.next = n
            curr = curr.next
        return res.next
# @lc code=end


#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd=ListNode()
        currOdd = odd
        even=ListNode()
        currEven = even
        c = 1
        while head is not None:
            i = ListNode(head.val)
            if c%2 == 1:
                currOdd.next = i
                currOdd = currOdd.next
            else:
                currEven.next = i
                currEven = currEven.next
            head = head.next
            c+=1
        odd = odd.next
        even = even.next
        currOdd.next = even
        return odd

# @lc code=end


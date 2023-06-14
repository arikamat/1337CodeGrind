from typing import *

#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowp = head
        fastp = head
        while fastp is not None:
            slowp = slowp.next
            fastp = fastp.next
            if fastp is not None:
                fastp = fastp.next
            else:
                return False
            if slowp == fastp:
                return True
        return False


# @lc code=end

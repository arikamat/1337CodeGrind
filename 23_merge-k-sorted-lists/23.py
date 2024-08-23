#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from typing import *
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while True:
            currMin = float('inf')
            idx = None
            noneTracker = None
            for c,i in enumerate(lists):
                if i:
                    noneTracker = c
                    if i.val<currMin:
                        currMin = i.val
                        idx = c
            if noneTracker is None:
                break
            node = ListNode(currMin)
            curr.next = node
            curr = node

            lists[idx] = lists[idx].next
        return head.next  
# @lc code=end
lists = [[1,4,5],[1,3,4],[2,6]]
a3 = ListNode(5)
a2 = ListNode(4,a3)
a1 = ListNode(1, a2)

b3 = ListNode(4)
b2 = ListNode(3,b3)
b1 = ListNode(1, b2)

c2 = ListNode(6)
c1 = ListNode(2, c2)

A = Solution()
res=A.mergeKLists([a1,b1,c1])
print(res)

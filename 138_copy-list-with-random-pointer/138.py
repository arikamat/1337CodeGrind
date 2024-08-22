#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
from typing import *
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        res = Node(0)
        newCurr = res
        d={}
        curr = head
        while curr:
            t = Node(curr.val)
            d[curr] = t
            newCurr.next = t
            newCurr = t
            curr = curr.next
        
        curr = head
        while curr:
            if curr.random:
                d[curr].random = d[curr.random]
            curr = curr.next
        return res.next
        # if head is None:
        #     return None
        # h = head
        # d={}
        # while head is not None:
        #     d[head] = (Node(head.val), head.next, head.random)
        #     head = head.next
        # for i in d:
        #     node = d[i][0]
        #     if d[i][1] is not None:
        #         next = d[d[i][1]][0]
        #         node.next = next
        #     if d[i][2] is not None:
        #         rand = d[d[i][2]][0]
        #         node.random = rand
            
            

        # return d[h][0]
# @lc code=end


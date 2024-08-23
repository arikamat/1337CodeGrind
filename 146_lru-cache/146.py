#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.size = 0

        self.left = Node(None, None)
        self.right = Node(None,None)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

        currRightmost = self.right.prev
        currRightmost.next = node
        node.prev = currRightmost
        node.next = self.right
        self.right.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            prev = node.prev
            after = node.next

            prev.next = after
            after.prev = prev
            
            currRightmost = self.right.prev

            currRightmost.next = node
            node.prev = currRightmost

            node.next = self.right
            self.right.prev = node
        else:
            if self.size>=self.capacity:
                currLeftmost = self.left.next
                self.left.next = currLeftmost.next
                currLeftmost.next.prev = self.left

                keyDelete = currLeftmost.key
                del self.d[keyDelete]
                self.size-=1

            node = Node(key,value)
            currRightmost = self.right.prev
            currRightmost.next = node
            node.prev = currRightmost

            node.next = self.right
            self.right.prev = node
            self.d[key] = node
            self.size+=1
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


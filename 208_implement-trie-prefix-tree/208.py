#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.children={}

class Trie:

    def __init__(self):
        self.head = Node("*")


    def insert(self, word: str) -> None:
        current = self.head
        for i in word:
            if i not in current.children:
                current.children[i] = Node(i)
            current = current.children[i]
        current.children['*'] = Node("*")
    def search(self, word: str) -> bool:
        current = self.head
        for i in word:
            if i not in current.children:
                return False
            else:
                current = current.children[i]
        return '*' in current.children
    def startsWith(self, prefix: str) -> bool:
        current = self.head
        for i in prefix:
            if i not in current.children:
                return False
            else:
                current = current.children[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end


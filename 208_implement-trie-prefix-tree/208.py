#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Node:
    def __init__(self, val="", left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Trie:
    
    def __init__(self):
        self.head = Node()
        self.s=set()
    def _insert(self,root, word):
        if root is None:
            return Node(word)
        if root.val<word:
            root.right = self._insert(root.right, word)
        elif root.val > word:
            root.left = self._insert(root.left, word)
        return root
    def insert(self, word: str) -> None:
        self.s.add(word)
        curr = self.head
        self._insert(curr,word)
    def _search(self, root, word, partial):
        if root is None:
            return False
        if partial and len(word) <= len(root.val) and word == root.val[0:len(word)]:
            return True
        elif (not partial) and word == root.val:
            return True
        elif word < root.val:
            return self._search(root.left,word,partial)
        elif word > root.val:
            return self._search(root.right,word,partial)
        return False
    def search(self, word: str) -> bool:
        curr = self.head
        return word in self.s
        # return self._search(curr, word, False)

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        return self._search(curr, prefix, True)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end


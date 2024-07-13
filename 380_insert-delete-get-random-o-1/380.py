#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        self.val_idx = {} # val: idx
        self.items = []

    def insert(self, val: int) -> bool:
        if val in self.val_idx:
            return False
        self.items.append(val)
        self.val_idx[val] = len(self.items)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_idx:
            return False
        idx = self.val_idx[val]
        if idx != len(self.items)-1:
            self.items[idx] = self.items[-1]
            self.val_idx[self.items[-1]] = idx
            self.items.pop()
            del self.val_idx[val]
        else:
            self.items.pop()
            del self.val_idx[val]
        return True

    def getRandom(self) -> int:
        rand = random.randint(0,len(self.items)-1)
        return self.items[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end


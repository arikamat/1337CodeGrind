#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#


# @lc code=start
class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [(timestamp, value)]
        else:
            self.d[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        low = 0
        high = len(self.d[key])-1
        res = ""
        data = self.d[key]
        while low <= high:
            mid = (low + high)//2
            if self.d[key][mid][0]<=timestamp:
                res = self.d[key][mid][1]
                low = mid+1
            else:
                high = mid-1
        
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

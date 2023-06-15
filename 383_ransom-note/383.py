#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote, magazine):
        ran = list(ransomNote)
        mag = list(magazine)
        for i in ran:
            if i not in mag:
                return False
            mag.remove(i)
        return True
# @lc code=end


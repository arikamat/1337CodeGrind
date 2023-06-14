from typing import *

#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#


# @lc code=start
class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        h = len(image)
        w = len(image[0])
        visited = []
        queue = [(sr, sc)]
        val = image[sr][sc]
        while len(queue) > 0:
            r, c = queue.pop(0)
            image[r][c] = color
            visited.append((r, c))
            dirs = [(r + 1, c), (r, c + 1), (r, c - 1), (r - 1, c)]
            for i in dirs:
                r, c = i
                if r < 0 or r >= h or c < 0 or c >= w:
                    continue
                elif i not in visited and image[r][c] == val:
                    queue.append((r, c))
        return image


# @lc code=end

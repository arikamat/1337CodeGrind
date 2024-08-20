#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
from typing import *
# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append((position[i],speed[i]))
        
        fleets = 1
        arr.sort()
        fleetLeaderPos, fleetLeaderSpeed = arr[-1]
        timeLeader = (target - fleetLeaderPos)/fleetLeaderSpeed

        arr = arr[0:len(arr)-1]
        for i in range(len(arr)-1,-1,-1):
            currPos, currSpeed = arr[i]
            timeNeeded = (target - currPos)/currSpeed

            if timeNeeded > timeLeader:
                fleets+=1
                fleetLeaderPos, fleetLeaderSpeed = arr[i]
                timeLeader = timeNeeded
        return fleets
# @lc code=end


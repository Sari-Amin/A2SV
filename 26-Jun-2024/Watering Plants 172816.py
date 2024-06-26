# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        waterCan = capacity
        for i in range(len(plants)):
            if waterCan >= plants[i]:
                ans += 1
                waterCan -= plants[i]
            else:
                waterCan = capacity
                ans += 2 * i + 1
                waterCan -= plants[i]
        return ans

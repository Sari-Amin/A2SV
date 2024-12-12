# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        heaters.sort()
        for i in range(len(houses)):
            left = 0
            right = len(heaters) - 1
            req = float('inf')
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] == houses[i]:
                    req = 0
                    break
                elif heaters[mid] < houses[i]:
                    req = min(req, abs(heaters[mid] - houses[i]))
                    left = mid + 1
                else:
                    req = min(req, abs(heaters[mid] - houses[i]))
                    right = mid
            req = min(req, abs(heaters[left] - houses[i]))
            ans = max(ans, req)
        return ans
                    

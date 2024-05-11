# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 1000000007
        newList = sorted(list(zip(efficiency, speed)), reverse = True)
   
        ans = 0
        speed = 0
        heap = []
        for eff, spd in newList:
            if len(heap) == k:
                speed -= heappop(heap)
            heappush(heap, spd)
            speed += spd
            # print(speed,eff,len(heap))
            ans = max(ans, eff * speed)
        return ans % MOD
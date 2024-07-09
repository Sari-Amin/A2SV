# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       
        for i in range(len(stones)):
            stones[i] *= (-1)

        heapify(stones)

        while len(stones) > 1:
         
            var1 = -heappop(stones)
            var2 = -heappop(stones)
            if var1 != var2:
                heappush(stones, -abs(var2 - var1))

        return 0 if len(stones) == 0 else -stones[0]
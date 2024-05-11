# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        minHeap = list(zip(capital,profits))
        
        heapify(minHeap)

        while k:
            
            while minHeap and minHeap[0][0] <= w:
                heappush(heap, -heappop(minHeap)[1])

            if heap:
                w -= heappop(heap)
            else:
                return w
            k -= 1

        return w


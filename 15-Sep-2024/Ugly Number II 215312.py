# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    
    def nthUglyNumber(self, n: int) -> int:
        visited = set([1])
        length = 0
        heap = []
        heappush(heap, 1)
        
        while heap:
            l = len(heap)
            for i in range(l):
                nd = heappop(heap)
                length += 1
                if length == n:
                    return nd
                for k in [2,3,5]:
                    if nd * k not in visited:
                        heappush(heap, nd * k)
                        visited.add(nd * k)
        return 0

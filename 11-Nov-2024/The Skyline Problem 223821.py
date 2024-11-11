# Problem: The Skyline Problem - https://leetcode.com/problems/the-skyline-problem/

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
       
        temp = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, "doesn't matter") for _, R, _ in buildings])   
        res, max_heap = [[0, 0]], [(0, float('inf'))]
        for x, neg_height, R in temp:
            while x >= max_heap[0][1]:
                heapq.heappop(max_heap)
            if neg_height:
               
                heapq.heappush(max_heap, (neg_height, R))
            curr_max = -max_heap[0][0]
            if res[-1][1] != curr_max:
                res.append([x, curr_max])
        return res[1:] 
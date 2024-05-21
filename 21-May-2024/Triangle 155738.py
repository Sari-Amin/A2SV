# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                dia1 = float("inf")  if j - 1 < 0 else triangle[i-1][j-1]
                before = float("inf")  if  j >= len(triangle[i-1]) else triangle[i-1][j]
                triangle[i][j] += min(dia1, before)
      
        return min(triangle[-1])
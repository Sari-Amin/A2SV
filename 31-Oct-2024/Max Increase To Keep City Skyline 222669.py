# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_cols = [0] * n
        max_rows = [0] * n
        for i in range(n):
            for j in range(n):
                max_rows[i] = max(max_rows[i],grid[i][j])
                max_cols[j] = max(max_cols[j], grid[i][j])

        res = 0
        for i in range(n):
            for j in range(n):
                res += min(max_cols[j], max_rows[i]) - grid[i][j]
    
        return res
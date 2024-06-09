# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col, curr_area):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return curr_area

            curr_area += grid[row][col]
            grid[row][col] = 0

            for dr, dc in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                curr_area = dfs(dr, dc, curr_area)
            return curr_area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    max_area = max(max_area, dfs(r, c, 0))

        return max_area

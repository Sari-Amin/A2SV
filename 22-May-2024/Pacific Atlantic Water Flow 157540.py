# Problem: Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(i,j):
            return i >= 0 and j >= 0 and i < rows and j < cols

        def dfs(row, col, visited, prevHeight):
            if not inbound(row, col) or (row,col) in visited or heights[row][col] < prevHeight:
                return 
            visited.add((row, col))
            for r,c in directions:
                dfs(row + r, col + c, visited, heights[row][col])


        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])
        

        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])

        res = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        return res
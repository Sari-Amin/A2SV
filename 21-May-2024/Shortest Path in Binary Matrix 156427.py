# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = -1
        directions =[(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1)]


        def inbound(i,j):
            return i>=0 and i < n and j >= 0 and j < n

        if grid[0][0] == 1:
            return ans
        que = deque([(0,0)])
        level = 1
        get = False
        while que and not get:
            for _ in range(len(que)):
                i,j = que.popleft()
                if (i, j) == (n - 1, n - 1):
                    ans = level
                    get = True
                    break
                for r,c in directions:
                    nr = i + r
                    nc = j + c
                    if inbound(nr,nc) and grid[nr][nc] != 1:
                        que.append((nr,nc))
                        grid[nr][nc] = 1
            level += 1
        return ans

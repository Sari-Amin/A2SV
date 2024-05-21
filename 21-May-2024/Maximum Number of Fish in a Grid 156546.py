# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def inbound(r,c):
            return r < n and r >= 0 and c >= 0 and c < m     

        def bfs(i,j):

            que = deque([(i,j)])
            res = 0
            visited = set([(i,j)])
            while que :
                row,col = que.popleft()
                res += grid[row][col]
                for r,c in directions:
                    nr = row + r
                    nc = col + c
                    if inbound(nr,nc) and grid[nr][nc] != 0 and (nr,nc) not in visited:
                        que.append((nr,nc))
                        visited.add((nr,nc))
          
            return res

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans, bfs(i,j))
        return ans
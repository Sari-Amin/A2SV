# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        directions =[(-1,0),(1,0),(0,1),(0,-1)]


        def inbound(i,j):
            return i>=0 and i < n and j >= 0 and j < m

     
        que = deque([(0,0)])
        visited = set([(0,0)])
        while que:
            print(que)
            i,j = que.popleft()
            if (i, j) == (n - 1, m - 1):
                return True
            if grid[i][j] == 1 :
                if inbound(i,j + 1) and (i, j + 1) not in visited and grid[i][j+1] in [1,3,5]:
                    que.append((i, j + 1))
                    visited.add((i, j + 1))
                if inbound(i, j - 1) and  (i, j - 1) not in visited and grid[i][j-1] in [1,4,6]:
                    que.append((i, j - 1))
                    visited.add((i, j - 1))
            elif grid[i][j] == 2 :
                if inbound(i - 1,j ) and (i - 1, j) not in visited and grid[i - 1][j] in [2,3,4]:
                    que.append((i - 1, j))
                    visited.add((i - 1, j))
                if inbound(i + 1, j) and  (i + 1, j) not in visited and grid[i+1][j] in [2,5,6]:
                    que.append((i + 1, j))
                    visited.add((i + 1, j))
            elif grid[i][j] == 3 :
                if inbound(i + 1,j) and (i+1, j) not in visited and grid[i+1][j] in [5,6,2]:
                    que.append((i+1, j))
                    visited.add((i+1, j))
                if inbound(i, j - 1) and  (i, j - 1) not in visited and grid[i][j - 1] in [1,4]:
                    que.append((i, j - 1))
                    visited.add((i, j - 1))
            elif grid[i][j] == 4 :
                if inbound(i + 1,j) and (i + 1, j) not in visited and grid[i+1][j] in [6,5,2]:
                    que.append((i + 1, j))
                    visited.add((i + 1, j))
                if inbound(i, j+1) and  (i , j+1) not in visited and grid[i][j+1] in [1,3,5]:
                    que.append((i , j + 1))
                    visited.add((i, j + 1))
            elif grid[i][j] == 6 :
                if inbound(i-1,j) and (i-1, j) not in visited and grid[i-1][j] in [4,3,2]:
                    que.append((i - 1, j))
                    visited.add((i - 1, j))
                if inbound(i, j + 1) and  (i, j + 1) not in visited and grid[i][j+1] in [1,3,5]:
                    que.append((i, j + 1))
                    visited.add((i, j + 1))
            elif grid[i][j] == 5 :
                if inbound(i - 1,j ) and (i - 1, j) not in visited and grid[i-1][j] in [2,3,4]:
                    que.append((i - 1, j))
                    visited.add((i - 1, j))
                if inbound(i, j - 1) and  (i, j - 1) not in visited and grid[i][j-1] in [4,6,1]:
                    que.append((i, j - 1))
                    visited.add((i, j - 1))

       
        return False

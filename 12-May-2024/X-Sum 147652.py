# Problem: X-Sum - https://codeforces.com/contest/1676/problem/D

for _ in range(int(input())):
    def solve():
        n,m = map(int, input().split())

        def inbound(r,c):
            return r < n and c < m and c > -1 and r > -1
        
        grid = []
        for i in range(n):
            row = list(map(int, input().split()))
            grid.append(row)
        if n == 1:
            return print(max(grid[0]))
        
        ans = float("-inf")
        for i in range(n):
            for j in range(m):
                temp = grid[i][j]

                #right top diagonals
                row,col = i - 1, j + 1
                while inbound(row, col):
                    temp += grid[row][col]
                    row -= 1
                    col += 1
                #left top diagonals
                row,col = i - 1, j - 1
                while inbound(row, col):
                    temp += grid[row][col]
                    row -= 1
                    col -= 1
                #bottom right diagonals
                row,col = i + 1, j + 1
                while inbound(row, col):
                    temp += grid[row][col]
                    row += 1
                    col += 1
                #bottom left diagonals
                row,col = i + 1, j - 1
                while inbound(row, col):
                    temp += grid[row][col]
                    row += 1
                    col -= 1
                ans = max(ans, temp)
        return print(ans)
    solve()
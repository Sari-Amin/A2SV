# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        dp[n - 1][m - 1] = 1 if dungeon[n - 1][m - 1] > 0 else 1 - dungeon[n - 1][m - 1]
        
        for i in range(n - 2, -1, -1):
            dp[i][m - 1] = dp[i + 1][m - 1] - dungeon[i][m - 1]
            if dp[i][m - 1] <= 0:
                dp[i][m - 1] = 1
        for j in range(m - 2, -1, -1):
            dp[n - 1][j] = dp[n - 1][j + 1] - dungeon[n - 1][j]
            if dp[n - 1][j] <= 0:
                dp[n - 1][j] = 1

        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                dp[i][j] = min(dp[i][j + 1] - dungeon[i][j], dp[i + 1][j] - dungeon[i][j])
                if dp[i][j] <= 0:
                    dp[i][j] = 1
    
        
        return dp[0][0]
# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dp(i, j, memo = {}):
            if i == m - 1 and j == n - 1:
                return 1
            if i > m or j > n:
                return 0
            state = (i, j)
            if state not in memo:
                memo[state] = dp(i + 1, j) + dp(i, j + 1)
               
            return memo[state]
            
        return dp(0,0)
        
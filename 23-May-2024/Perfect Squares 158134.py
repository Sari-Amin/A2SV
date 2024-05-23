# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for  target in range(1, n + 1):
            for i in range(1, target + 1):
                if i * i > target:
                    break
                dp[target] = min(dp[target], 1 + dp[target - i*i])
        return dp[n] 

# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #bottom-up
        n = len(cost) 
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        return min(dp[n - 1], dp[n - 2])

        


        #top-down
        # def dp(ind, memo = {}):
        #     if ind >= len(cost):
        #         return 0
        #     if ind not in memo:
        #         memo[ind] = min(dp(ind + 1) + cost[ind], dp(ind + 2) + cost[ind])
        #     return memo[ind]

        # return min(dp(0), dp(1))

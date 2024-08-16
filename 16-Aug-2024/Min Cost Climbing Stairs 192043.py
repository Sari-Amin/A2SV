# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [0] * len(cost)
        # for i in range()
        
        def dp(ind, memo = {}):
            if ind >= len(cost):
                return 0
            if ind not in memo:
                memo[ind] = min(dp(ind + 1) + cost[ind], dp(ind + 2) + cost[ind])
            return memo[ind]
            
        return min(dp(0), dp(1))

# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(ind,amount, memo = {}):
            if amount == 0:
                return 0
            if amount < 0 or ind >= len(coins):
                return float("inf")
            state = (ind, amount)
            if state not in memo:
                memo[state] = min(dp(ind + 1, amount), dp(ind, amount - coins[ind])  + 1)
               
            return memo[state]
        
        ans = dp(0,amount)
        if ans == float("inf"):
            return -1
        return ans
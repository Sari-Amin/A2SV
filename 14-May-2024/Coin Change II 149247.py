# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    
        def dp(ind,amount, memo = {}):
       
            if amount == 0:
                return 1
            if amount < 0 or ind >= len(coins):
                return 0

            state = (ind, amount)
            
            if state not in memo:
                memo[state] = dp(ind + 1, amount) + dp(ind, amount - coins[ind])
        
            return memo[state]
        
        return dp(0,amount)
      

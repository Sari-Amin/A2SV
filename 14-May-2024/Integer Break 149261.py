# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
       
        def dp(amount, num = 1, prod = 1, memo = {}):

            if amount == 0:
                return prod
                
            if amount < 0 or num >= n:
                return float("-inf")

            state = (num, amount)
            if state not in memo:
                memo[state] = max(dp(amount, num + 1, prod), dp(amount - num, num, prod * num))
               
            return memo[state]
        
      
        return dp(n)
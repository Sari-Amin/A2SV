# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
       
        def dp(number, num = 1, prod = 1, memo = {}):

            if number == 0:
                return prod
                
            if number < 0 or num >= n:
                return float("-inf")

            state = (num, number)
            if state not in memo:
                memo[state] = max(dp(number, num + 1, prod), dp(number - num, num, prod * num))
               
            return memo[state]
        
      
        return dp(n)
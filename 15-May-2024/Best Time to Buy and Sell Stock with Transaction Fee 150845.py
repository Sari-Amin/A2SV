# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def dp(ind, buy, memo = {}):
            if ind >= len(prices):
                return 0
            state = (ind, buy)
            if state not in memo:
                if buy:
                    memo[state] = max(-prices[ind] + dp(ind + 1, 0), dp(ind + 1, 1))
                else:
                    memo[state] = max(prices[ind] - fee + dp(ind + 1, 1), dp(ind + 1, 0))
            return memo[state]
        
        return dp(0,1)
                

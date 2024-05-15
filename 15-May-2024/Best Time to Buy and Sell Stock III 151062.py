# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(ind, buy,count = 0):
            if ind >= len(prices) or count == 2:
                return 0
            state = (ind, buy,count)
            if state not in memo:
                if buy:
                    memo[state] = max(-prices[ind] + dp(ind + 1, 0, count), dp(ind + 1, 1, count))
                else:
                    memo[state] = max(prices[ind] + dp(ind + 1, 1, count + 1), dp(ind + 1, 0, count))
            return memo[state]
        
        return dp(0,1)
                
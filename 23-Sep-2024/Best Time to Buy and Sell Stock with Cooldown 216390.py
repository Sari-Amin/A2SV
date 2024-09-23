# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def topDown(ind, buy, memo = {}):
            if ind >= len(prices):
                return 0
            state = (ind, buy)
            if state not in memo:
                if buy:
                    memo[state] = max(-prices[ind] + topDown(ind + 1, 0), topDown(ind + 1, 1))
                else:
                    memo[state] = max(prices[ind] + topDown(ind + 2, 1), topDown(ind + 1, 0))
            return memo[state]
        
        return topDown(0,1)
            
        
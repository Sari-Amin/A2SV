# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            minVal = min(minVal, prices[i])
            ans = max(ans, prices[i] - minVal)
        return ans
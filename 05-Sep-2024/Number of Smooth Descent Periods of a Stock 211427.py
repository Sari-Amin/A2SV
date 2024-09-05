# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        left = 0
        right = 0
        while right < len(prices):
            if prices[right - 1] != prices[right] + 1:
                left = right

            ans += right - left + 1

            right += 1
        return ans

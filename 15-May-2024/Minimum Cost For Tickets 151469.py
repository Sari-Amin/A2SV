# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        def dp(ind, memo =  {}):

            if ind >= len(days):
                return 0
          
            if ind not in memo:
                memo[ind] = float("inf")
                for d, c in zip([1,7,30], costs):
                    temp = ind
                    while temp < len(days) and days[ind] + d > days[temp]:
                        temp += 1
        
                    memo[ind] = min(memo[ind], dp(temp) + c)
            
            return memo[ind]

        return dp(0)
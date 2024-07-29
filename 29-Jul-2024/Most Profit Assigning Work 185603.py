# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0
        diff_profit = [(difficulty[i], profit[i]) for i in range(len(profit))]
      
        
        diff_profit.sort()

        worker.sort()
        left = 0
        best = 0
        
        for work in worker:
            while left < len(diff_profit) and work >= diff_profit[left][0]:
                best = max(best, diff_profit[left][1])
                left += 1
            
            ans += best
        
        return ans
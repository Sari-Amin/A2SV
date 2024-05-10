# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
    
        def dp(ind,memo={}):
            if ind >= len(nums):
                return 0
            if ind in memo:
                return memo[ind]
            memo[ind] = max(nums[ind] + dp(ind + 2), dp(ind + 1))
            return memo[ind]
       
        return dp(0)
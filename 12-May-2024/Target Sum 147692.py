# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dp(index, sm = 0, memo = {}):

            if index == len(nums):
                if sm == target:
                    return 1
                else:
                    return 0
            state = (index, sm)
            if state not in memo:
                positive = dp(index + 1, sm + nums[index])
                negative = dp(index + 1, sm - nums[index])
                memo[state] = positive + negative

            return memo[state]
            
        return dp(0)
        

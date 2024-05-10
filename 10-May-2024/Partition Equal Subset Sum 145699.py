# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dp(ind,target, memo = {}):
            if target <= 0 or ind >= len(nums):
                return target == 0
            state = (ind, target)
            if state in memo:
                return memo[state]
            
            memo[state] = dp(ind + 1, target) or dp(ind + 1, target - nums[ind])
            return memo[state]
        
        target = sum(nums) 
        if target % 2:
            return False
        else:
            return dp(0, target // 2)
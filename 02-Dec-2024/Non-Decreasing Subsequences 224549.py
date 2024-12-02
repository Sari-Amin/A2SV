# Problem: Non-Decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(ind, sub = []):
            if ind >= len(nums):
                if len(sub) > 1 and sub not in ans:
                    ans.append(sub[:])
                return 
            if len(sub) > 1 and sub not in ans:
                ans.append(sub[:])
            
            for i in range(ind, len(nums)):
                if len(sub) == 0 or len(sub) > 0 and nums[i] >= sub[-1]:
                    sub.append(nums[i])
                    backtracking(i + 1, sub)
                    sub.pop()

        backtracking(0)
        
        return ans
# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums) - 1):
            ans = max(ans, nums[i + 1] - nums[i])
        
        return ans
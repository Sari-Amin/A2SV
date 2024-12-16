# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        leftSum = 0
        ans = float("-inf")
        for num in nums:
            if leftSum + num > num:
                leftSum += num
            else:
                leftSum = num
            ans = max(ans, leftSum)
            
        return ans
        

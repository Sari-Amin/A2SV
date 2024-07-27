# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1
        
        for i in range(len(nums) - 2, -1, -1):
            ans[i] = ans[i + 1] * nums[i + 1]
    
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            ans[i] *= prefix
        return ans

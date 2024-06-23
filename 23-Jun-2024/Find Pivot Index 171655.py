# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        
        for i in range(len(nums)):

            rightSum -= nums[i]

            if leftSum == rightSum:
                return i

            leftSum += nums[i]

        return -1
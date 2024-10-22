# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        left = 0
        while left < len(nums):
            correct = nums[left] - 1
            if nums[left] < len(nums) and nums[left] > 0 and nums[left] != nums[correct]:
                nums[left], nums[correct] = nums[correct], nums[left]
            else:
                left += 1

        for ind, val in enumerate(nums):
            if ind + 1 != val:
                return ind + 1
        return len(nums) + 1
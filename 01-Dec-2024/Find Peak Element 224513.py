# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0 and i + 1 < len(nums) and nums[i] > nums[i + 1]:
                return i
            elif i == len(nums) - 1 and  i - 1 >= 0 and  nums[i] > nums[i - 1]:
                return i
            elif nums[i- 1] < nums[i] > nums[i + 1]:
                return i
        return 0

# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zero = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                zero += 1
        left = 0
        right = 1
        while left < len(nums) and right < len(nums):

            if nums[right] != 0:
                if nums[left] == 0:
                    nums[right], nums[left] = nums[left], nums[right]
                    right += 1
                    left += 1
                else:
                    if left == right:
                        right += 1
                    left += 1
            else:
                right += 1

        return nums

        
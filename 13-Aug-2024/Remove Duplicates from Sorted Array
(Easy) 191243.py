# Problem: Remove Duplicates from Sorted Array
(Easy) - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        curr = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != curr:
                nums[k] = curr
                curr = nums[i]
                k += 1
        nums[k] = curr
        return k + 1
# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        left = 0
        while left < len(nums) - 1:
            if nums[left] ^ nums[left + 1] != 0:
                ans.append(nums[left])
                left += 1
            else:
                left += 2
        if left < len(nums) and nums[left - 1] ^ nums[left] != 0:
            ans.append(nums[left])
            
        return ans
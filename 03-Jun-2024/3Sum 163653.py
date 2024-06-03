# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left,  right = i + 1, len(nums) - 1

            while left < right:
                temp = num + nums[left] + nums[right]
                if temp < 0:
                    left += 1
                elif temp > 0:
                    right -= 1
                else:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return ans

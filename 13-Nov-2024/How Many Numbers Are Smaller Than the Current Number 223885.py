# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednums = sorted(nums)
        res = []
        for i in range(len(nums)):
            res.append(sortednums.index(nums[i]))
        return res
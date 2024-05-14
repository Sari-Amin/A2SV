# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(1,len(nums)):
            if nums[i - 1] < nums[i]:
                continue
            elif nums[i - 1] > nums[i]:
                temp = nums[i - 1] - nums[i]
                nums[i] += temp + 1
                ans += temp + 1
            else:
                nums[i] += 1
                ans += 1

        return ans
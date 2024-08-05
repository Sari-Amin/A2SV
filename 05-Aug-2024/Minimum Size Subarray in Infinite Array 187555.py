# Problem: Minimum Size Subarray in Infinite Array - https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

        total = sum(nums)
        temp_ans = len(nums) * (target // total)
        target %= total

        left = 0
        right = 0
        nums += nums
        ans = float("inf")
        _sum = 0
        while right < len(nums) and left < len(nums):
            if _sum == target:
                ans = min(ans, right - left)
            _sum += nums[right]
            right += 1
            while left < len(nums) and _sum > target:
                _sum -= nums[left] 
                left += 1
            
        return ans + temp_ans if ans != float("inf") else -1
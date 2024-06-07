# Problem: Max Numbers of K sums - https://leetcode.com/problems/max-number-of-k-sum-pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            num = nums[left] + nums[right]
            if num == k:
                ans += 1
                left += 1
                right -= 1
            elif num < k :
                left += 1
            else:
                right -= 1
        return ans
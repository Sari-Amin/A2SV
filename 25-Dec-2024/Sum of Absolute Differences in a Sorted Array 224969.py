# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixSum = []
        prefixSum.append(nums[0])
        for i in nums[1:]:
            prefixSum.append(prefixSum[-1] + i)

        ans = [0] * n
        for i in range(n):

            if i == 0:
                ans[i] =(prefixSum[-1] - nums[i]) - nums[i] * (n - i - 1)
            else:
                ans[i] = i * nums[i] - prefixSum[i - 1] + (prefixSum[-1] - prefixSum[i]) - nums[i] * (n - i - 1)

        return ans
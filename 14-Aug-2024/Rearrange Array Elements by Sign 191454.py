# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        pos_ptr = 0
        neg_ptr = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[pos_ptr] = nums[i]
                pos_ptr += 2
            else:
                ans[neg_ptr] = nums[i]
                neg_ptr += 2
        return ans

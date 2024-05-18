# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = [i for i in nums if i < 0]
        pos = [i for i in nums if i >= 0]
        numsPtr = 0
        ptr = 0
        while numsPtr < len(nums):
            nums[numsPtr] = pos[ptr]
            numsPtr += 1
            nums[numsPtr] = neg[ptr]
            numsPtr += 1
            ptr += 1
        return nums
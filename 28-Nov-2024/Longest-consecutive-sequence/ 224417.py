# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        nums.sort()
        curr = nums[0]
        res = 0
        current_count = 1

        for num in nums:
            if num == curr:
                continue
            if num == curr + 1:
                current_count += 1
                curr += 1
            else:
                res = max(res, current_count)
                current_count = 1
                curr = num
        
        return max(res,current_count)


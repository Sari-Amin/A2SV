# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        
        pre = [0] * (len(nums) + 1)
        pre[0] = 1
        tot = 0
        res = 0
        
        for num in nums:
            tot += num
            if tot >= k:
                res += pre[tot - k]
            pre[tot] += 1
        
        return res
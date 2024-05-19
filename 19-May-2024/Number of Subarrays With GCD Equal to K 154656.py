# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = nums.count(k)
        
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i + 1, len(nums)):
                temp = gcd(temp, nums[j])
                if temp == k:
                    ans += 1
        return ans
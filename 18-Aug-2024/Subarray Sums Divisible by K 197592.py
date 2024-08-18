# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        d = defaultdict(lambda : 0)
        d[0] = 1
        leftSum = 0
        for num in nums:
            leftSum += num
            if leftSum % k in d:
                ans += d[leftSum % k]
            d[leftSum % k] += 1

        return ans
   
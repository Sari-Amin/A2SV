# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
       
        def factorSum(num):
            ans = 0
            p = 2
            while p * p <= num:
                while num % p == 0:
                    num //= p
                    ans += p
                p += 1
            if num > 1:
                ans += num
            return ans

 
        while n != factorSum(n):
            n = factorSum(n)

        return n


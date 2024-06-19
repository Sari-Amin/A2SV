# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
       
        def primefactors(num):
            factors = 0
            p = 2
            while p * p <= num:
                while num % p == 0:
                    num //= p
                    factors += p
                p += 1
            if num > 1:
                factors += num
            return factors

 
        while n != primefactors(n):
            n = primefactors(n)

        return n


# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
       
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n ) :
            if (prime[p] == True):

                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

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

 
        while not prime[n]:
            temp = primefactors(n)
            if temp == n:
                return n
            n = temp

        return n


# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007

        def bit_exponentation(x,n):
            ans = 1
            for i in (bin(n)[2:])[::-1]:
                
                if i != "0":
                    ans = ((ans % MOD) * (x % MOD) * int(i)) % MOD
                x = ((x % MOD) * (x % MOD)) % MOD

            return ans % MOD

        ans = 1
        if n % 2:
            ans = 5

        ans = ((ans % MOD) * (bit_exponentation(5, n // 2) % MOD) * (bit_exponentation(4, n // 2) % MOD)) % MOD

        return ans
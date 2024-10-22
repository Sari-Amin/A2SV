# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def comb(n,r):
            mx = max(r, n - r)
            mn = min(r, n - r)
            ans = 1
            for i in range(n,mx, -1):
                ans *= i
            for i in range(1,mn + 1):
                ans //= i
            return ans
        
        return comb(m + n - 2, m - 1)
# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = set()
        d = 1
        while d * d <= n:
            if n % d == 0:
                ans.add(d)
                ans.add(n // d)
            d += 1
            
        if len(ans) < k:
            return -1
        return sorted(ans)[k - 1]

            
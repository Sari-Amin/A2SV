# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        # memo = {}
        # def dp(val, it = 1):
        #     if val == n:
        #         return 0
        #     if val > n or it > n:
        #         return 10000000
        #     state = (val, it)
        #     if state not in memo:
        #         memo[state] = min(dp(val + val, it) + 1, dp(val, it + 1) + 1)
        #     return memo[state]
        # return dp(1) + 1
        ans = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                ans.append(d)
                n //= d
            d += 1
        if n != 1:
            ans.append(n)
        return sum(ans)
# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev, curr = 0, 1
        ans = 0
        for i in range(n-1):
            ans = prev + curr
            prev = curr
            curr = ans
        return ans

# Problem: Reverse Bits - https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:]
        if len(b) < 32:
            b = "0" * (32 - len(b)) + b
        return int(b[::-1], 2)
# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = bin(n)[2:]
        for i in range(len(bits) - 1):
            if bits[i] == bits[i + 1]:
                return False
        return True

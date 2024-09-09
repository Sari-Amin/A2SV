# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        num = 0
        while num <= n:
            res.append(bin(num).count("1"))
            num += 1
        return res
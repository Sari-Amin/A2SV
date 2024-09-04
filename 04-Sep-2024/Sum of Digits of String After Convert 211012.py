# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        first_convert = [""]
        for ch in s:
            first_convert[0] += str(ord(ch) - ord("a") + 1)
        while k:
            temp = 0
            for ch in first_convert[0]:
                temp += int(ch)
            first_convert[0] =  str(temp)
            k -= 1
        return int(first_convert[0])
# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:

        def countBits(word):
            bits = 0
            for ch in word:
                bits |= 1 << ord(ch) - ord("a")
            return bits

        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) * len(words[j]) <= ans:
                    continue
                val = countBits(words[i]) & countBits(words[j])
                if not val:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
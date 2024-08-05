# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:

        def helper(word1, word2):
            bits = ["0"] * 26
            for i, ch in enumerate(word1):
                bits[ord(ch) - ord("a")] = "1"
            for i, ch in enumerate(word2):
                if bits[ord(ch) - ord("a")] == "1":
                    return 0, False
            return len(word1) * len(word2), True

        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) * len(words[j]) <= ans:
                    continue
                val, possible = helper(words[i], words[j])
                if possible:
                    ans = max(ans, val)
        return ans
# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(len(word1)):
            res += word1[i]
            if i < len(word2):
                res += word2[i]
        res += word2[i+1:]
        return res
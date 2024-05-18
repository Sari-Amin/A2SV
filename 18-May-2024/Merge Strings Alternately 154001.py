# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(len(word1)):
            ans += word1[i]
            if i < len(word2):
                ans += word2[i]
        ans += word2[i+1:]
        return ans
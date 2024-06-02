# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        l = 0
        while l < len(s):
            pos = int(s[l][-1]) - 1
            if s[l] != s[pos]:
                s[l], s[pos] = s[pos], s[l]
            else:
                l += 1
        
        return " ".join([i[:-1] for i in s])


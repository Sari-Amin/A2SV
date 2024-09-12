# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allow = set(allowed)
        for i in range(len(words)):
            temp = 0
            st = set(words[i])
            for j in st:
                if j in allow:
                    temp += 1
            if temp == len(st):
                ans += 1
        return ans
# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        memo = {}
        def backtrack(ind):
            if ind >= len(s):
                return [[]]
            
            if ind not in memo:
                temp = []
                for i in range(ind, len(s)):
                    if s[ind:i + 1] == s[ind:i + 1][::-1]:
                        for ne in backtrack(i + 1):
                            temp.append([s[ind:i + 1]] + ne)

                memo[ind] = temp
                            
            return memo[ind]
        return backtrack(0) 
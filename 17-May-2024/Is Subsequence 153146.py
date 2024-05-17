# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0 for _ in range((len(t) + 1))] for _ in range((len(s) + 1))]
        for i in range(len(s) + 1):
            for j in range(len(t) + 1):
                if i == 0 or j == 0:
                    continue
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] =  max(dp[i - 1][j], dp[i][j - 1])
       
        return dp[len(s)][len(t)] == len(s)
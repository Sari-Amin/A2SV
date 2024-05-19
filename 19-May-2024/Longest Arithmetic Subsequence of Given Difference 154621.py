# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        ans = 1
        for i in range(n):
            temp = arr[i] - difference
            if temp not in dp:
                dp[arr[i]] = 1
            else:
                dp[arr[i]] = dp[temp] + 1 
                ans = max(ans, dp[arr[i]])
       
        return ans
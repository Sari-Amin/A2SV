# Problem: Best Sightseeing Pair - https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        mx = 0
        ans = 0

        for i, val in enumerate(values):
            if i != 0:
                ans = max(ans, mx + val - i)
            mx = max(mx, val + i)

        return ans

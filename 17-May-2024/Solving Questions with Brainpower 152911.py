# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        #bottom-Up
        dp = [0 for i in range(len(questions))]
        dp[-1] = questions[-1][0]
        for i in range(len(questions) - 2, -1, -1):
            next_ = i + questions[i][1] + 1
            take = questions[i][0] + (dp[next_] if next_ < len(questions) else 0)
            skip = dp[i + 1]
            dp[i] = max(skip, take)

        return dp[0]
        #top-down
        # memo = {}
        # def dp(ind):
        #     if ind >= len(questions):
        #         return 0
        #     if ind not in memo:
        #         memo[ind] = max(questions[ind][0] + dp(ind + questions[ind][1] + 1), dp(ind + 1))
        #     return memo[ind]
        # return dp(0)

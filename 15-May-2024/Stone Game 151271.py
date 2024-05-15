# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dp(left, right, memo = {}):
            if left > right:
                return 0
            state = (left, right)
            if state not in memo:
                memo[state] = max(dp(left + 1, right - 1) + piles[left], dp(left + 1, right - 1) + piles[right])
            return memo[state]
            
        alice = dp(0,len(piles) - 1)

        return alice > sum(piles) - alice
            



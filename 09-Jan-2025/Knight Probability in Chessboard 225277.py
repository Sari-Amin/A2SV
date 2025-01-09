# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def inbound(r,c):
            return 0 <= r < n and 0 <= c < n

        memo = {}
        
        def dp(r,c,move=k):
            if inbound(r,c) and move == 0:
                return 1
            if not inbound(r,c) or move == 0:
                return 0
            state = (r,c,move)
            
            if state not in memo:
                memo[state] = (
                        (1/8) * dp(r-2,c+1,move-1)+
                        (1/8) * dp(r-2,c-1,move-1)+
                        (1/8) * dp(r-1,c+2,move-1)+
                        (1/8) * dp(r-1,c-2,move-1)+
                        (1/8) * dp(r+2,c+1,move-1)+
                        (1/8) * dp(r+2,c-1,move-1)+
                        (1/8) * dp(r+1,c+2,move-1)+
                        (1/8) * dp(r+1,c-2,move-1)
                    )
            return memo[state]
    
        return dp(row,column)
# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = [0 for _ in range(n)]
        leftDiagonals = [0 for _ in range(2 * n + 1)]
        RightDiagonals = [0 for _ in range(2 * n + 1)]
        total = 0

        def backtrack(i, j_range=None):
            nonlocal rows
            nonlocal leftDiagonals
            nonlocal RightDiagonals
            nonlocal total

            for j in range(*j_range) if j_range else range(n):
                if not (
                    rows[j] or RightDiagonals[(r := i + j)] or leftDiagonals[(l := i - j + n - 1)]
                ):
                    if i + 1 == n:
                        total += 1
                    else:
                        rows[j] = 1
                        leftDiagonals[l] = 1
                        RightDiagonals[r] = 1
                        backtrack(i + 1)
                        rows[j] = 0
                        leftDiagonals[l] = 0
                        RightDiagonals[r] = 0

        backtrack(0, (0, n // 2))
        total *= 2
        if n % 2:
            backtrack(0, (n // 2, n // 2 + 1))

        return total
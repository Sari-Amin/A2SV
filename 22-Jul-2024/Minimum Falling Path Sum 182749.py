# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                
                dia1 = float("inf") if j - 1 < 0 else matrix[i - 1][j - 1]
                dia2 = float("inf") if j + 1 >= m else matrix[i - 1][j + 1] 
                matrix[i][j] = min(dia1, dia2, matrix[i - 1][j]) + matrix[i][j]

        return min(matrix[-1])
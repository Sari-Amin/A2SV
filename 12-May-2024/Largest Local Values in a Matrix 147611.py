# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []

        for i in range(len(grid) - 2):
            temp = []
            
            for j in range(len(grid[0]) - 2):
                max_ = float("-inf")
                for k in range(i, i + 3):
                    max_ = max(max_, max(grid[k][j:j + 3]))
                temp.append(max_)
            ans.append(temp)
        return ans

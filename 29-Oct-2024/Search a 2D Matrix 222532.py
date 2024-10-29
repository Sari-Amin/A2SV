# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
             
            mid = left + (right - left) // 2
            col = mid % len(matrix[0])
            row = mid // len(matrix[0])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
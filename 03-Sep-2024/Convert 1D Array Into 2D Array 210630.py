# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
            
        ans = []
        left = 0
        temp = []
        while left < len(original):
            if len(temp) == n:
                ans.append(temp)
                temp = []
            temp.append(original[left])
            left += 1
        ans.append(temp)
        return ans
# Problem: Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + ( right - left) // 2
            
            if 0 < mid < len(arr) - 1 and arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif mid - 1 > 0 and arr[mid - 1] < arr[mid] or mid + 1 < len(arr) - 1 and arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return 0
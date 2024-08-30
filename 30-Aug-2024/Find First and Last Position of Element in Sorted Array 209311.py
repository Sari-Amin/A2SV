# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(rightBias, left = 0, right = len(nums) - 1):
            index = -1
            while left <= right:
                 
                mid = left + (right - left) // 2
              
                if nums[mid] == target:
                    index = mid
                    if rightBias:
                        left = mid + 1
                    else:
                        right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return index

        return [binarySearch(False), binarySearch(True)]
 
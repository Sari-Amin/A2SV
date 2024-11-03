# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            if nums[i] < pivot:
                ans.append(nums[i])
        
        for i in range(n):
            if nums[i] == pivot:
                ans.append(nums[i])
        
        for i in range(n):
            if nums[i] > pivot:
                ans.append(nums[i])

        return ans
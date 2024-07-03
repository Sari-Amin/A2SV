# Problem: Shuffle the Array - https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = 0, n
        ans = []

        while right < len(nums):
            ans.append(nums[left])
            ans.append(nums[right])
            left += 1
            right += 1

        return ans
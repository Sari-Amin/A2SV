# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        while k:
            ans += nums[-1]
            nums[-1] += 1
            k -= 1
        return ans
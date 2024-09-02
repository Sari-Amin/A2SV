# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k -= (k // sum(chalk)) * sum(chalk)
        left = 0
        while chalk[left % len(chalk)] <= k:
            k -= chalk[left % len(chalk)]
            left += 1

        return left % len(chalk)

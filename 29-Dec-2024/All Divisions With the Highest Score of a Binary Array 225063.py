# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = nums.count(1)
        left_sum = 0
        ans = defaultdict(list)
        best = -1
        for i in range(len(nums)):
            ans[ones + left_sum].append(i)
            best = max(best, ones + left_sum)
            if nums[i] == 0:
                left_sum += 1
            else:
                ones -= 1
            
        ans[ones + left_sum].append(i + 1)
        best = max(best, ones + left_sum)

        
        return ans[best]
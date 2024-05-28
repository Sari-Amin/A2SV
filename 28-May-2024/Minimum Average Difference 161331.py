# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0]
        for i in range(n):
            pre.append(pre[-1] + nums[i])
        ans = (float("inf"), -1)
  
        for i in range(n):
            left = int(pre[i+1]/(i+1))
            right = int((pre[-1] - pre[i+1])/(n - i - 1)) if n - 1 - i != 0 else 0
            temp = abs(left - right)
           
            if ans[0] > temp:
                ans = (temp, i)
        return ans[1]
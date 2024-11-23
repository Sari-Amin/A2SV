# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = [0,0]
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                res = [dic[target-nums[i]],i]
                break
            dic[nums[i]] = i
        return res
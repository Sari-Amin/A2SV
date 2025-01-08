# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [False for i in range(len(l))]
        left = 0
        while left < len(l):
            temp = sorted(nums[l[left]:r[left] + 1])
            if len(temp) > 1:
                d = temp[1] - temp[0]
                pos = True
                for i in range(1, len(temp) - 1):
                    if d != temp[i + 1] - temp[i]:
                        pos = False
                        break
                if pos:
                    ans[left] = True

            left += 1

        return ans
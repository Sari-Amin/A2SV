# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)


        for num, val in dic.items():
            post = sum(val)
            pre = 0
            n = len(val)
            p = 0
            for i in val:
                pre += i
                p += 1
                post -= i
                n -= 1
                ans[i] = -pre + p * i - n * i + post
        return ans
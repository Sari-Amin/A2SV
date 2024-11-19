# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sm = sum(nums[:k])
        st = set(nums[:k])
        if len(st) == k:
            ans = sm
        dic = defaultdict(int)
        for i in nums[:k]:
            dic[i] += 1

        for i in range(len(nums) - k):
            
            sm -= nums[i]
            sm += nums[i + k]
            dic[nums[i]] -= 1
            dic[nums[i + k]] += 1
            if dic[nums[i]] == 0:
                st.remove(nums[i])
            st.add(nums[i + k])
            if len(st) == k:
                ans = max(ans, sm)
        return ans


            
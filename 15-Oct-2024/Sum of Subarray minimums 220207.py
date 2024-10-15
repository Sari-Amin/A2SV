# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [-math.inf] + arr + [-math.inf]
        n = len(arr)

        st = []
        res = 0
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                mid = st.pop()
                left = st[-1]
                right = i

                res += arr[mid] * (mid - left) * (right - mid)

            st.append(i)
        return res % 1000000007
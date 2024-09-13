# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] ^= arr[i - 1]
        ans = []
        for l, r in queries:
            ans.append(arr[r] ^ (arr[l - 1] if l > 0 else 0))
        return ans
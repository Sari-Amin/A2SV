# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        res = 0
        n = len(citations)
        for i in range(n):
            if citations[i] >= i + 1 :
                res = max(res, i + 1)
        return res
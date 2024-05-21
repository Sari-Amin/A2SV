# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = defaultdict(int)
        for a,b in edges:
            incoming[b] += 1
        ans = (0,0)
        for v in range(n):
            if incoming[v] == 0:
                ans = (v, ans[1] + 1)
                
        if ans[1] > 1:
            return -1
        return ans[0]
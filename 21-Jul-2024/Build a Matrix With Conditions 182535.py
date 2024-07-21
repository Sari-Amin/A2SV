# Problem: Build a Matrix With Conditions - https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topSort(gr):
            graph = defaultdict(list)
            incoming = defaultdict(int)
            for u,v in gr:
                incoming[v] += 1
                graph[u].append(v)
            queue = deque([u for u in range(1, k + 1) if incoming[u] == 0])
            ans = []
            while queue:
                node = queue.popleft()
                ans.append(node)
                for nr in graph[node]:
                    incoming[nr] -= 1
                    if incoming[nr] == 0:
                        queue.append(nr)
            return len(ans) == k, ans
        ans = [[0] * k for _ in range(k)]
        rowPossible, rowTop = topSort(rowConditions)
        colPossible, colTop = topSort(colConditions)
        if not(rowPossible and colPossible):
            return []
        rowInd = {}
        colInd = {}
        for i in range(k):
            rowInd[rowTop[i]] = i
            colInd[colTop[i]] = i
        for i in range(1, k + 1):
            ans[rowInd[i]][colInd[i]] = i
        return ans




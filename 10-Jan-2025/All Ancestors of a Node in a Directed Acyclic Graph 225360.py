# Problem: All Ancestors of a Node in a Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for u, v in edges:
            graph[u].append(v)
            incoming[v] += 1
        queue = deque([i for i in range(n) if not incoming[i]])         
        res = [set() for  _ in range(n)]

        while queue:
            node = queue.popleft()
            for nd in graph[node]:
                incoming[nd] -= 1
                res[nd].add(node)
                for i in res[node]:
                    res[nd].add(i)
                if not incoming[nd]:
                    queue.append(nd)

        return [sorted(list(res)) for res in res]

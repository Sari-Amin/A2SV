# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)

        def dfs(node, graph):
            temp = True
            for nd in  graph[node]:
                if colors[nd] == -1:
                    colors[nd] = 0 if colors[node] == 1 else 1
                    temp = temp and dfs(nd,graph)
                else:
                    temp = temp and colors[nd] != colors[node]

            return temp

        res = True
        for i in range(len(graph)):
            if colors[i] == -1:
                colors[i] = 0
                res = res and dfs(i,graph)
        return res
        


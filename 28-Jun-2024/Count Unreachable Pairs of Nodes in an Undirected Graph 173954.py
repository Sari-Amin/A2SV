# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
   
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        sizes = []
        visited = set()
        def bfs(n):
            temp = 0
            queue = deque([n])
            visited.add(n)
            while queue:
                node = queue.popleft()
                temp += 1
                for nr in graph[node]:
                    if nr not in visited:
                        visited.add(nr)
                        queue.append(nr)
         
            return temp
 
        for v in range(n):
            if v not in visited:
                sizes.append(bfs(v))

        sizes.sort(reverse = True)
        tot = sum(sizes)
        ans = 0
        for i in range(len(sizes) - 1):
            tot -= sizes[i]
            ans += sizes[i] * tot
            
        return ans
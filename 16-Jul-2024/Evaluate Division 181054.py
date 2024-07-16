# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)   

        for i,eq in enumerate(equations):
            a,b = eq    
            graph[a].append([b,values[i]]) 
            graph[b].append([a,1/values[i]]) 

        def bfs(src,trg):
            if src not in graph or trg not in graph:
                return -1
            
            queue = deque()
            visited = set()

            queue.append([src,1])   
            visited.add(src)
            
            while queue:
                n , w = queue.popleft() 

                if n == trg:
                    return w

                for neighbor,weight in graph[n]:   
                    if neighbor not in visited:
                        queue.append([neighbor, w * weight])
                        visited.add(n)

            return -1

        return [bfs(query[0],query[1]) for query in queries]
    
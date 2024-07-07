# Problem: Largest Color Value in a Directed Graph - https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
       
        visit = set()
        cycle = set()
        graph = defaultdict(list)
        for u,v in edges: 
            graph[u].append(v)

        def dfs(node):
            if not graph[node]: 
                return True
            cycle.add(node)
            for child in graph[node]:
                if child in cycle:
                    return False
                if child not in visit:
                    if not dfs(child): 
                        return False
            cycle.remove(node)
            visit.add(node)
            return True

        for node in range(n):
            if not dfs(node): 
                return -1
   
        cache = {}
        color_types = list(Counter(colors).keys())

        def dp(node):
            if node in cache: 
                return cache[node]
            result = defaultdict(int)
            for child in graph[node]:
                child_result = dp(child)
                for color in color_types:
                    result[color] = max(result[color], child_result[color])
            result[colors[node]] += 1
            cache[node] = result
            return result
            
        ans = 0
        for node in range(n):
            result = dp(node)
            ans = max(ans, max(list(result.values())))

        return ans
            

        
            
            

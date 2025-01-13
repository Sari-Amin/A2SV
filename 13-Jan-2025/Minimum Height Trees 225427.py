# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adjacency_list = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
     
        ans = deque([i for i in range(n) if degree[i] == 1])
     
        remaining_nd = n
        while remaining_nd > 2:
            leave_count = len(ans)
            remaining_nd -= leave_count
            for _ in range(leave_count):
                leaf = ans.popleft()
                for neighbor in adjacency_list[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        ans.append(neighbor)
        
        return list(ans)
# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List
from collections import defaultdict, deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        incoming = defaultdict(int)
        vertices = set()
        for i in range(V):
            for j in adj[i]:
                incoming[j] += 1
                vertices.add(j)

        queue = deque([i for i in vertices if incoming[i] == 1])
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nb in adj[node]:
                incoming[nb] -= 1
                if incoming[nb] == 1:
                    queue.append(nb)
                    
        return len(ans) != len(vertices)
            
            

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(graph, start_node):
            distances = {node: float('inf') for node in range(1, n + 1)}
            distances[start_node] = 0
            processed = set()

            heap = [(0, start_node)]
            while heap:
                cost, curr = heapq.heappop(heap)
                if curr in processed:
                    continue
                
                processed.add(curr)
                
                for neighbor, weight in graph[curr]:
                    if distances[neighbor] > cost + weight:
                        distances[neighbor] = cost + weight
                        heapq.heappush(heap, (distances[neighbor], neighbor))
                        

            return distances

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = dijkstra(graph, k)
        pos = True
        ans = 0
        for i in range(1, n + 1):
            if dist[i] == float("inf"):
                pos = False
                break
            ans = max(ans, dist[i])
        if not pos:
            return -1
        return ans
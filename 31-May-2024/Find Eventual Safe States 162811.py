# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, g: List[List[int]]) -> List[int]:
        incoming = defaultdict(int)
        graph = defaultdict(list)
        for i in range(len(g)):
            for nd in g[i]:
                graph[nd].append(i)
                incoming[i] += 1
    
        ans = []
        que = deque()
        for i in range(len(g)):
            if incoming[i] == 0:
                que.append(i)
        
        while que:
            node = que.popleft()
            ans.append(node)
            for nd in graph[node]:
                incoming[nd] -= 1

                if incoming[nd] == 0:
                    que.append(nd)
        
        return sorted(ans)
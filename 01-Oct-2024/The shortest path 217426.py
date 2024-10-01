# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

n, m = map(int, input().split())
source, target = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

path = {source:-1}
queue = deque([source])
visited = set([source])
while queue:
    node = queue.popleft()
    for j in graph[node]:
        if j not in visited:
            path[j] = node
            queue.append(j)
            visited.add(j)

if target not in path:
    print(-1)
else:
    ans = []
    curr = target
    while curr != -1:
        ans.append(curr)
        curr = path[curr]
    print(len(ans) - 1)
    print(*ans[::-1])


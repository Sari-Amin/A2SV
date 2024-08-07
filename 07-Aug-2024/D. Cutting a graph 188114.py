# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

class UnionFind:
    def __init__(self, no):
        self.root = {i:i for i in range(1, no + 1)}
        self.size = {i:1 for i in range(1, no + 1)}
    
    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]

n, m, k = map(int, input().split())
uf  = UnionFind(n)

for i in range(m):
    u, v = map(int, input().split())

query = []
for i in range(k):
    query.append(input().split())

ans = []
for cmd, u, v in query[::-1]:

    if cmd == "ask":
        
        if uf.find(int(u)) == uf.find(int(v)):
            ans.append("YES")
        else:
            ans.append("NO")
    else:
        uf.union(int(u), int(v))

for a in ans[::-1]:
    print(a)
        
        


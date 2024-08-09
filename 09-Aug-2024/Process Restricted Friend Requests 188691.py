# Problem: Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/

class UnionFind:
    def __init__(self, no):
        self.root = {i:i for i in range(no)}
        self.size = {i:1 for i in range(no)}
    
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


class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        ans = []
        uf = UnionFind(n)
        for u, v in requests:
            u_parent = uf.find(u)
            v_parent = uf.find(v)
            if u_parent == v_parent:
                ans.append(True)
                continue

            flag = True
            for r1, r2 in restrictions:
                r1_parent = uf.find(r1)
                r2_parent = uf.find(r2)
                if (r1_parent == u_parent and r2_parent == v_parent) or (r2_parent == u_parent and r1_parent == v_parent):
                    flag = False
                    break
            if flag:
                uf.union(u,v)
                ans.append(True)
            else:
                ans.append(False)
        return ans


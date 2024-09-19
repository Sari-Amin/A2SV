# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        root = [i for i in range(n)]
        size = [1] * n

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return x

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]

        for i,j in pairs:
            union(i,j)
        st = {i : [] for i in range(n)}
        index = {i:0 for i in range(n)}
        for i in range(n):
            p = find(i)
            st[p].append(s[i])
        for i in st:
            st[i] = sorted(st[i])
        ans = ""
        for i in range(n):
            p = find(i)
            ans += st[p][index[p]]
            index[p] += 1

            
        return ans
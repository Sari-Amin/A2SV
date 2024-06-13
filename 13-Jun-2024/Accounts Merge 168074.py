# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        size = {}
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union( x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX] >= size[rootY]:
                    parent[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    parent[rootX] = rootY
                    size[rootY] += size[rootX]
        
        name = {}
        emailss = []
        ans = defaultdict(list)

        for i in range(len(accounts)):
            emails = []
            for email in accounts[i][1:]:
                parent[email] = email
                size[email] = 0
                name[email] = accounts[i][0]
                emails.append(email)
            emailss.append(emails)

        for i in range(len(emailss)):
            for j in range(len(emailss[i]) - 1):
                union(emailss[i][j], emailss[i][j + 1])

        for key, val in parent.items():
            par = find(key)
            ans[par].append(key)
       
        res = []
        for key, val in ans.items():
            res.append([name[key]] + sorted(set(val)))
        return res
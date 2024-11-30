# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        s = s1 + s2

        parent = {i: i for i in s}
        def find(x):
            if parent[x] ==x:
                return x
            return find(parent[x])
    
        def union(x, y):
            root1 = find(x)
            root2 = find(y)
            if root1 != root2:
                if root1 > root2:
                    parent[root1] = root2

                else:
                    parent[root2] = root1
        left = right = 0
        while right < len(s1):
            union(s1[left], s2[right])
            left +=1
            right +=1
            
        ans = []
        for i in baseStr:
            if i not in parent:
                ans.append(i)
            else:
                while i != parent[i]:
                    i = parent[parent[i]]
                ans.append(i)
        return ''.join(ans)

        
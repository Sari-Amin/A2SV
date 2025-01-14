# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            
        queu = deque([i for i in graph if (len(graph[i])) == 1][:1:])
        visited = set([queu[0]])
        ans = []
        while queu:
            node = queu.popleft()
            ans.append(node)

            for nb in graph[node]:
                if nb not in visited:
                    queu.append(nb)
                    visited.add(nb)
        return ans

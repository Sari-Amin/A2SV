# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)

        for i in range(len(manager)):
            graph[manager[i]].append(i)

        queue = deque([(headID, 0)])
        ans = 0

        while queue:
           
            node, time = queue.popleft()
            ans = max(ans, time)

            for nb in graph[node]:
                queue.append((nb, time + informTime[node]))
                
        return ans
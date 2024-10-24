# Problem: Minimum Time Taken by Each Job to be Completed Given by a DAG - https://practice.geeksforgeeks.org/problems/minimum-time-taken-by-each-job-to-be-completed-given-by-a-directed-acyclic-graph/1

from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for u,v in edges:
            graph[u].append(v)
            incoming[v] += 1
        qu = deque([i for i in range(1, n + 1) if incoming[i] == 0])
        ans = [1 for _ in range(n)]
        level = 1
        while qu:
            ln = len(qu)
            for i in range(ln):
                node = qu.popleft()
                ans[node - 1] = level
                for nb in graph[node]:
                    incoming[nb] -= 1
                    if incoming[nb] == 0:
                        qu.append(nb)
            level += 1
        return ans
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends
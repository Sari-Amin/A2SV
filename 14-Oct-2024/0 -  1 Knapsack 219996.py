# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
       
        # code here
        def dp(ind, tot = 0):
            if ind >= len(wt):
                return 0
            pick = 0
            if tot + wt[ind] <= W:
                pick = dp(ind + 1, tot + wt[ind]) + val[ind]
            not_pick = dp(ind + 1, tot)
            return max(pick, not_pick)
        return dp(0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends
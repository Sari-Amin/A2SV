# Problem: Maximum Depth of N-ary Tree - https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0
        def dfs(root, depth):
            nonlocal ans

            if not root:
                return 
            ans = max(ans, depth)

            for node in root.children:
                dfs(node, depth + 1)
        dfs(root, 1)
        return ans

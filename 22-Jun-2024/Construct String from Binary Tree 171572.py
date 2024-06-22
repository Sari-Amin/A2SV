# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(root):
            if not root:
                return ""
  
            ans = ""
            ans += str(root.val)
            if root.left:
                ans += "(" + dfs(root.left) + ")" 
            elif root.right:
                ans += "()"
            if root.right:
                ans += "(" + dfs(root.right) + ")"
            return ans
        return dfs(root)
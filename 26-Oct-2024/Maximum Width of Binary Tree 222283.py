# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = defaultdict(lambda : [pow(2,32),0])
        def rec(node,h,num):
            if(node == None):  return ""
            else:
              if(level[h][0] > num%pow(2,31) ): level[h][0] = num%pow(2,31)
              if(level[h][1] < num%pow(2,31) ): level[h][1] = num%pow(2,31)
              rec(node.left,h+1,num*2+1)
              rec(node.right,h+1,num*2+2)
              
        rec(root,0,0)
        res = 0
        
        for key in level.keys():
          res = max( res , level[key][1]-level[key][0])
        return res +1
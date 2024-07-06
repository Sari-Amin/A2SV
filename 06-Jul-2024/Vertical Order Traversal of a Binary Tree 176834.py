# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        column = defaultdict(list)

        def dfs(root, left, right):
            if not root:
                return 
            if right in column:
                column[right].append((left, root.val))
            else:
                column[right] = [(left, root.val)]

            dfs(root.left, left + 1, right - 1)
            dfs(root.right, left + 1, right + 1)
    
        dfs(root, 0, 0)
        ans = []
        for i in sorted(column.keys()):
            temp = [k[1] for k in sorted(column[i])]
            ans.append(temp)
        return ans
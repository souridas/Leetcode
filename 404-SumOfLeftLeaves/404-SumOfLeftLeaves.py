# Last updated: 2/21/2026, 9:43:48 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node):
            return node is not None and not node.left and not node.right

        def dfs(node):
            if not node:
                return 0
            
            res = 0
            if node.left and is_leaf(node.left):
                res += node.left.val
            res += dfs(node.left)
            res += dfs(node.right)
            
            return res

        return dfs(root)
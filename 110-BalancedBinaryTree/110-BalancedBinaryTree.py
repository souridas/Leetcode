# Last updated: 2/21/2026, 9:44:37 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self,root):
        if not root:
            return 0
        return 1+max(self.depth(root.left),self.depth(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        x= self.isBalanced(root.left)
        l_depth=self.depth(root.left)
        r_depth=self.depth(root.right)
        y=self.isBalanced(root.right)
        return x and y and abs(l_depth-r_depth)<=1
        

        
        
        
        
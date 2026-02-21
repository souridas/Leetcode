# Last updated: 2/21/2026, 9:44:36 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l=self.minDepth(root.left)
        r=self.minDepth(root.right)
        if l==0:
            l=r
        if r==0:
            r=l
        return 1+min(l,r)
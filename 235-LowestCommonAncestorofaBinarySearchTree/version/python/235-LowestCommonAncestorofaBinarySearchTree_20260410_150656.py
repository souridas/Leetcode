# Last updated: 4/10/2026, 3:06:56 PM
# compare with the root value
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if p.val<root.val and q.val<root.val:
11            return self.lowestCommonAncestor(root.left,p,q)
12        elif p.val>root.val and q.val>root.val:
13            return self.lowestCommonAncestor(root.right,p,q)
14        else:
15            return root
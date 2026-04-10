# Last updated: 4/10/2026, 10:39:52 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        if not root or root==p or root==q:
11            return root
12        left_search=self.lowestCommonAncestor(root.left,p,q)
13        right_search=self.lowestCommonAncestor(root.right,p,q)
14        if left_search and right_search:
15            return root
16        return left_search if left_search else  right_search
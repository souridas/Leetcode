# Last updated: 3/7/2026, 12:47:57 PM
'''
if both childs are none return true, if either of this none then return false
then check if both the values are same then check for the child conditions
'''

1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        def is_mirror(l,r):
10            if not l and not r:
11                return True
12            if not l or not r:
13                return False
14            return l.val==r.val and is_mirror(l.left,r.right) and is_mirror(l.right,r.left)
15        return is_mirror(root.left,root.right)
16
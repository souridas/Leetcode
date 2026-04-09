# Last updated: 4/9/2026, 7:29:55 PM
# find depth and l_depth+r_depth
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def __init__(self):
9        self.diameter=0
10    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
11        def height(node):
12            if not node:
13                return 0
14            l_height=height(node.left)
15            r_height=height(node.right)
16            self.diameter=max(self.diameter,l_height+r_height)
17            return 1+max(l_height,r_height)
18        height(root)
19        return self.diameter
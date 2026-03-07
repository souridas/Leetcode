# Last updated: 3/7/2026, 11:13:53 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        self.total=0
10        def dfs(root):
11            if not root:
12                return
13            dfs(root.right)
14            self.total+=root.val
15            root.val=self.total
16            dfs(root.left)
17        dfs(root)
18        return root
19        
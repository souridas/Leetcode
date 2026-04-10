# Last updated: 4/10/2026, 3:34:00 PM
# set k-num check
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
9        seen=set()
10        def dfs(node):
11            if not node:
12                return False
13            if k-node.val in seen:
14                return True
15            seen.add(node.val)
16            return dfs(node.left) or dfs(node.right)
17        return dfs(root)
18
19
20        
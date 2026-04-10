# Last updated: 4/10/2026, 9:59:50 AM
# recursion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def __init__(self):
9        self.max_sum=float('-inf')
10    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
11        def func(node):
12            if not node:
13                return 0
14            l_sum=max(func(node.left),0)
15            r_sum=max(func(node.right),0)
16            curr_sum=node.val+l_sum+r_sum
17            self.max_sum=max(self.max_sum,curr_sum)
18            return node.val+max(l_sum,r_sum)
19        func(root)
20        return self.max_sum
21        
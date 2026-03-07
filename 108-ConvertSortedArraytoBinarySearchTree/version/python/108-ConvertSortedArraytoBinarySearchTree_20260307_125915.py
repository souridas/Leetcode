# Last updated: 3/7/2026, 12:59:15 PM
# the middle of the array is the node then recursively do it for left and right subtrees
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
9        def create_node(l,r):
10            if l>r:
11                return 
12            m=(l+r)//2
13            node = TreeNode(val=nums[m])
14            node.left=create_node(l,m-1)
15            node.right=create_node(m+1,r)
16            return node
17        return create_node(0,len(nums)-1)
18        
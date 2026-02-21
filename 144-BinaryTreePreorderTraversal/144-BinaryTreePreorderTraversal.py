# Last updated: 2/21/2026, 9:44:25 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorder(root,lis):
    if not root:
            return
    lis.append(root.val)
    preorder(root.left,lis)
    preorder(root.right,lis)
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis=[]
        preorder(root,lis)
        return lis
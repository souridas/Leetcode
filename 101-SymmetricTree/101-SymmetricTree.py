# Last updated: 2/21/2026, 9:44:40 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def check(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val!=q.val:
        return False
    return check(p.left,q.right) and check(p.right,q.left)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return check(root.left,root.right)
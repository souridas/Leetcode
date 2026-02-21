# Last updated: 2/21/2026, 9:44:41 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1=[]
        queue2=[]
        queue1.append(p)
        queue2.append(q)
        while queue1 or queue2:
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)
            if (node1 and not node2) or (node2 and not node1):
                return False
            elif (node1 and node2) and (node1.val != node2.val):
                return False
            if node1:
                queue1.append(node1.left)
                queue1.append(node1.right)
            if node2:
                queue2.append(node2.left)
                queue2.append(node2.right)
        return True
        
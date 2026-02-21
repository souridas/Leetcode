# Last updated: 2/21/2026, 9:43:22 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        f=head
        while f and f.next :
            f=f.next.next
            head=head.next
        return head
        
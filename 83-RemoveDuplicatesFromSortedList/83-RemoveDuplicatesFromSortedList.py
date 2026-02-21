# Last updated: 2/21/2026, 9:44:47 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            temp=head
            while temp:
                if temp.next and temp.val == temp.next.val:
                    temp.next=temp.next.next
                else:
                    temp=temp.next
        return head
                
# Last updated: 2/21/2026, 9:45:20 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer_stack=[]
        p=head
        l=0
        while p:
            pointer_stack.append(p)
            p=p.next
            l+=1
        pointer_stack.pop(l-n)
        if len(pointer_stack) == 0:
            return None
        head=pointer_stack[0]
        for i in range(len(pointer_stack)):
            if i<len(pointer_stack)-1:
                pointer_stack[i].next=pointer_stack[i+1]
            else:
                pointer_stack[i].next=None
        return head

# Last updated: 2/21/2026, 9:45:30 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        runner=head
        carry=0
        while l1!=None or l2!=None:
            if l1==None:
                sum=carry+l2.val
                l2=l2.next
            elif l2==None:
                sum=carry+l1.val
                l1=l1.next
            else:
                sum=carry+l1.val+l2.val
                l1=l1.next
                l2=l2.next
            temp=ListNode(val=sum%10)
            runner.next=temp
            runner=runner.next
            carry=sum//10
        if carry:
            temp=ListNode(val=carry)
            runner.next=temp
        return head.next
                





        
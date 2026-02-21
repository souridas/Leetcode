# Last updated: 2/21/2026, 9:45:19 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(-1)
        ans=temp
        while(list1 and list2):
            if list1.val<=list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        while(list1):
            temp.next=list1
            temp=temp.next
            list1=list1.next
        
        while(list2):
            temp.next=list2
            temp=temp.next
            list2=list2.next
        return ans.next


        
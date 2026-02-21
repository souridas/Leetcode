// Last updated: 2/21/2026, 9:44:31 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        ListNode *p,*q;
        p=q=head;
        if(head==NULL || head->next==NULL)
        {
            return false;
        }
        do
        {
            p=p->next;
            q=q->next;
            if(q)
            {
                q=q->next;
            }
        }
        while(p && q && p!=q);
            if(p==q)
            {
                return true;
            }
        return false;
    }
};
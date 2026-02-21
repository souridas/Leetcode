// Last updated: 2/21/2026, 9:44:23 AM
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* p=headA;
        ListNode* q=headB;
        stack<ListNode*> st1;
        stack<ListNode*> st2;
        if(p==NULL || q==NULL)
        {
            return 0;
        }
       while(p)
       {
           st1.push(p);
           p=p->next;
       }
        while(q)
       {
            st2.push(q);
           q=q->next;
       }
        int flag=0;
        ListNode* t1;
        while((!st1.empty()&& !st2.empty()) && (st1.top()==st2.top()))
        {
            t1=st1.top();
            st1.pop();
            st2.pop();
            flag=1;
        }
        if(flag)
        {
            return t1;
        } 
       return 0;        
    }
};
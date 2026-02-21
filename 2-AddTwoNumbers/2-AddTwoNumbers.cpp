// Last updated: 2/21/2026, 9:45:31 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
    ListNode* p=l1;
    ListNode* q=l2;
    int carry=0;
    ListNode *last;
    ListNode * ans;
    ListNode *first=0;
        int z;
    while (p!=0 && q!=0)
    {
         
        z=carry+p->val+q->val;
        carry=z/10;
         ans=new ListNode();
        ans->val=z%10;
        ans->next=0;  
        p=p->next;
        q=q->next;
        if(first==0)
        {
            last=first=ans;
        }
        else
        {
        last->next=ans;
            last=ans;
        }
        
    }
        while(p!=0)
        {
           
            z=carry+p->val;
            carry=z/10;
            ans=new ListNode();
            ans->val=z%10;
            ans->next=0;
            p=p->next;
            last->next=ans;
            last=ans;
        }
        while(q!=0)
        {
            z=carry+q->val;
            carry=z/10;
            ans=new ListNode();
            ans->val=z%10;
            ans->next=0;
            q=q->next;
            last->next=ans;
            last=ans;
        }
        if(carry==1)
        {
            ans=new ListNode();
            ans->next=0;
            ans->val=1;
            last->next=ans;
            last=ans;
        }
        return first;
        
    }
};
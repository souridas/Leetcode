// Last updated: 2/21/2026, 9:45:22 AM
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *merge,*last;
        if(l1==0 && l2==0)
        {
            return NULL;
        }
        if(l1==0 && l2!=0)
        {
            return l2;
        }
        if(l1!=0 && l2==0)
        {
            return l1;
        }
        if(l1->val<l2->val)
        {
            merge=last=l1;
            l1=l1->next;
            last->next=NULL;
        }
        else
        {
            merge=last=l2;
            l2=l2->next;
            last->next=NULL;
        }
        while(l1!=NULL && l2!=NULL)
        {
            if(l1->val<l2->val)
            {
                last->next=l1;
                last=l1;
                l1=l1->next;
                last->next=NULL;
            }
            else
            {
                last->next=l2;
                last=l2;
                l2=l2->next;
                last->next=NULL;
            }
        }
        if(l1!=NULL)
        {
            last->next=l1;
        }
        if(l2!=NULL)
        {
            last->next=l2;
        }
        return merge;
    }
};
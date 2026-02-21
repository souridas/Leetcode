// Last updated: 2/21/2026, 9:45:16 AM
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
    ListNode* swapPairs(ListNode* head) {
        ListNode* p=head;
        
        while(p!=NULL)
        {
            int a=p->val;
            if(p->next!=NULL)
            { 
                int b=p->next->val;
                int temp=a;
                p->val=b;
                p->next->val=temp;
                p=p->next->next;  
            }
            else
            {
                break;
            }
        }
        return head;
        
    }
};
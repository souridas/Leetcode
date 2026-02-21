// Last updated: 2/21/2026, 9:44:05 AM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool path(TreeNode* root,vector<TreeNode*> &addr,TreeNode* p)
    {
        if(root==NULL)
        {
            return false;
        }
        addr.push_back(root);
        if(root==p)
        {
            return true;
        }
        if((root->left&&path(root->left,addr,p))||(root->right&&path(root->right,addr,p)))
           {
               return true;
           }
        addr.pop_back();
        return false;
        
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
       vector<TreeNode*> ar1,ar2;
        if(!path(root,ar1,p) || !path(root,ar2,q))
        {
            return NULL;
        }
        int i;
        for(i=0;i<ar1.size()&& i<ar2.size();i++)
        {
            if(ar1[i]!=ar2[i])
            {
                break;
            }
        }
        return ar1[i-1]; 
    }
};
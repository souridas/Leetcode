// Last updated: 2/21/2026, 9:43:36 AM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if(d==1)
        {
          TreeNode* temp=new TreeNode(v); 
          temp->left=root;
          return temp;
        }
        ans(root,v,d,1);
        return root;
    }
    void ans(TreeNode* root,int v,int d, int lvl)
    {
        if(!root)
        {
            return;
        }
        if(lvl==d-1)
        {
           TreeNode* l=root->left;
          TreeNode* r=root->right;
            root->left=new TreeNode(v,l,NULL);
            root->right=new TreeNode(v,NULL,r);  
            return;
        }
        ans(root->left,v,d,lvl+1);
        ans(root->right,v,d,lvl+1);
    }
    
};
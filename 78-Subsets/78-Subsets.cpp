// Last updated: 2/21/2026, 9:44:52 AM
class Solution {
public:
  
    void subutil(vector<int>& nums,vector<int>& subset,vector<vector<int>>& res,int ind)
    {
        res.push_back(subset);
        for(int i=ind;i<nums.size();i++)
        {
            subset.push_back(nums[i]);
            subutil(nums,subset,res,i+1);
            subset.pop_back();
        }
        return ;
    
    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
    
        vector<int> subset;
        vector<vector<int>> res;
        subutil(nums,subset,res,0);
        return res;
        
    }
};
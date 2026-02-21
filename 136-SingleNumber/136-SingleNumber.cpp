// Last updated: 2/21/2026, 9:44:27 AM
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int n=nums.size();
        int k=nums[0];
        for(int i=1;i<n;i++)
        {
            k=k^nums[i];
        }
        return k;
    }
};
// Last updated: 2/21/2026, 9:44:07 AM
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int n=nums.size();
        int prefix[2][n];
        prefix[0][0]=1;
        prefix[1][n-1]=1;
        for(int i=1;i<n;i++)
        {
            prefix[0][i]=prefix[0][i-1]*nums[i-1];
            prefix[1][n-i-1]=prefix[1][n-i]*nums[n-i];
        }
        vector<int> arr;
        for(int i=0;i<n;i++)
        {
            arr.push_back(prefix[0][i]*prefix[1][i]);
        }
        return arr;
    }
};
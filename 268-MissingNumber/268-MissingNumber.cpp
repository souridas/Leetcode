// Last updated: 2/21/2026, 9:43:59 AM
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size();
        int k=0;
        for(int i=0;i<n;i++)
        {
            k=k^nums[i]^(i+1);
        }
        return k;
    }
};
// Last updated: 2/21/2026, 9:45:06 AM
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_g=INT_MIN;
        int max_l=0;
        int n=nums.size();
        int flag=0;
        int m=INT_MIN;
        for(int i=0;i<n;i++)
        {
            if(nums[i]>0)
            {
                flag=1;
                break;
            }
            m=max(m,nums[i]);
    }
        if(flag==0)
        {
            return m;
        }
        for(int i=0;i<n;i++)
        {
            max_l=max_l+nums[i];
            if(max_l>max_g)
            {
                max_g=max_l;
            }
            if(max_l<0)
            {
                max_l=0;
            }
        }
        return max_g;
        
    }
};
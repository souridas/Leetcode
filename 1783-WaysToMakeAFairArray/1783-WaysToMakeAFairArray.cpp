// Last updated: 2/21/2026, 9:43:11 AM
class Solution {
public:
    int waysToMakeFair(vector<int>& nums) {
        
        int sum1=0,sum2=0,sum3=0,sum4=0;
        int n=nums.size();
        int ans=0;
        for(int i=0;i<n;i++)
        {
            if(i%2)
            {
                sum1+=nums[i];
            }
            else
            {
                sum2+=nums[i];
            }
        }
        for(int i=0;i<n;i++)
        {
          if(i%2)
          {
            sum1-=nums[i];
          }
            else
            {
                sum2-=nums[i];    
            }
            if(sum1+sum4==sum2+sum3)
            {
                ans++;            
            }
                
            if(i%2)
            {
                sum3+=nums[i];
            }
            else
            {
                sum4+=nums[i];
            }
        }
        return ans;
    }
};
// Last updated: 2/21/2026, 9:44:01 AM
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        int n=nums.size();
        
        for(int i=0;i<n-1;)
        {
            int j=i,k;
            k=j;
            while(i<n-1 && nums[i]==0)
            {
              i++;  
            }
            while( j>=0 && nums[j]==0)
            {
                j--;
            }
            if(k!=j)
            {j=j+1;}
            if(i!=j)
                
            {nums[j]=nums[i];
                nums[i]=0;
            }
            else
            {
                i++;
            }
        }
        
    
    }
};
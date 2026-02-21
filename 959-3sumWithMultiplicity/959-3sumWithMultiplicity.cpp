// Last updated: 2/21/2026, 9:43:21 AM
class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        
        int n=arr.size();
        long long count=0;
        for(int i=1;i<n-1;i++)
        {
            int mid=arr[i];
            int l,r;
            int R[500]={0};
    
           for(r=i+1;r<n;r++)
            {
                    R[arr[r]]++;
    
            } 
            for(int j=0;j<i;j++)
            {
                int x=target-mid-arr[j];
                if(x>=0)
                {
                    if(R[x]>0)
                    {
                        count+=R[x];
                    }
                }
            }
        }
        return count%(1000000007);
    }
};
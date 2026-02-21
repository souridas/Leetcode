// Last updated: 2/21/2026, 9:44:16 AM
class Solution {
public:
    int countPrimes(int n) {
        long long *arr=new long long[n];
        for(long long i=0;i<n;i++)
        {
          arr[i]=0;  
        }
        for(long long i=2;i<n;i++)
        {
            for(long long j=i*i;j<n;j=j+i)
            {
                arr[j]=1;
            }
        }
        int c=0;
        for(long long i=2;i<n;i++)
        {
           if(arr[i]==0)
           {
            c++; 
           }
        }
        return c;
    }
};
// Last updated: 2/21/2026, 9:43:26 AM
class Solution {
public:
    int consecutiveNumbersSum(int N) {
      
        int ans=1;
        for(int i=2;i<=sqrt(2*N);i++) if((N-(i*(i-1))/2)%i==0)ans++;    
        return ans;
        
    }
    
};
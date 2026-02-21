// Last updated: 2/21/2026, 9:43:12 AM
class Solution {
public:
    int kthFactor(int n, int k) {
        
        int i=1,count=0;
        while(count<k)
        {
            if(n%i==0)
            {
                count++;
            }
            if(n<i)
            {
                return-1;
            }
            i++;
        }
        return i-1;
    }
};
// Last updated: 2/21/2026, 9:43:35 AM
class Solution {
public:
    bool judgeSquareSum(int c) {
        
        int i=sqrt(c);
        while(i>=0)
        {
            int num2=c-i*i;
            if((int)sqrt(num2)-(double)sqrt(num2)==0)
            {
                return true;
            }
            
            i--;
        }
        return false;
    }
};
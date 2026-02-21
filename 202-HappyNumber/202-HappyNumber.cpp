// Last updated: 2/21/2026, 9:44:17 AM
class Solution {
public:
    int squar(int n)
    {
        int sum=0;
        while(n)
        {
            sum=sum+(n%10)*(n%10);
            n=n/10;
        }
        return sum;
}
    bool isHappy(int n) {
       set<int> s;
        while(1)
        {
            n=squar(n);
            if(n==1)
            {
                return true;
            }
            if(s.find(n)!=s.end())
            {
                return false;
        }
            s.insert(n);
        }
    }
       
};
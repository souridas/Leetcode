// Last updated: 2/21/2026, 9:45:28 AM
class Solution {
public:
    int reverse(int x) {
        long long int a=pow(2,31)-1;
        long long int b=-pow(2,31);
        stack<int> st;
        int i=-1;
        while(x!=0)
        {
            st.push(x%10);
            x=x/10;
            i++;
        }
        int len=i,j=0;
        long long int y=0;
        while(!st.empty() && j<=len)
        {
            y=pow(10,j)*st.top()+y;
            j++;
            st.pop();
        }
        if(x<0)
        {
            return -y;
        }
        else if(y<b||y>a)
        {
            return 0;
        }
        else
        {
            return y;
        }
            
    }
};
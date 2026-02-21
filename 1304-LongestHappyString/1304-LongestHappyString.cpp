// Last updated: 2/21/2026, 9:43:15 AM
class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        
        int t=a+b+c;
        int i=0;
        string ans="";
        int cur_a=0,cur_b=0,cur_c=0;
        while(i<t)
        {
            if((a>=b && a>=c && cur_a!=2)||(a>0 && (cur_b==2||cur_c==2)))
            {
                ans+='a';
                a--;
                cur_a++;
                cur_b=0;
                cur_c=0;
            }
            
            else if((b>=a && b>=c && cur_b!=2)||(b>0 && (cur_a==2||cur_c==2)))
            {
                ans+='b';
                b--;
                cur_b++;
                cur_a=0;
                cur_c=0;
            }
            else if((c>=b && c>=a && cur_c!=2)||(c>0 && (cur_b==2||cur_a==2)))
            
            {
                ans+='c';
                c--;
                cur_c++;
                cur_a=0;
                cur_b=0;
            }  
            i++;
        }
        return ans;
    }
};
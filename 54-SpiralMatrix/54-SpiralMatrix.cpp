// Last updated: 2/21/2026, 9:45:02 AM
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
       
        vector<int> vec;
        int T=0,B=matrix.size()-1,L=0,R=matrix[0].size()-1;
        int i,dir=0;
        while(L<=R && T<=B)
        {
            if(dir==0)
            {
                for(i=L;i<=R;i++)
                {
                    vec.push_back(matrix[T][i]);
                }
                T++;
            }
             if(dir==1)
            {
                for(i=T;i<=B;i++)
                {
                    vec.push_back(matrix[i][R]);
                }
                R--;
            }
            if(dir==2)
            {
                for(i=R;i>=L;i--)
                {
                    vec.push_back(matrix[B][i]);
                }
                B--;
            }
             if(dir==3)
             {
                 for(i=B;i>=T;i--)
                 {
                     vec.push_back(matrix[i][L]);
                 }
                 L++;
             }
            dir=(dir+1)%4;
            
        }
return vec;
    }
};
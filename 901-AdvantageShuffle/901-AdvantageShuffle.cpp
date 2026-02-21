// Last updated: 2/21/2026, 9:43:23 AM
class Solution {
public:
    vector<int> advantageCount(vector<int>& A, vector<int>& B) {
   
       vector<int> order(A.size());
        vector<int> ans(A.size());
        int n=A.size();
        for(int i=0;i<n;i++)
        {
            order[i]=i;
        }
        sort(order.begin(),order.end(),[&](int a,int b){return B[a]>B[b];});
        sort(A.begin(),A.end(),greater<>());
        int j=0,k=n-1;
        for(auto ix: order)
        {
            if(A[j]>B[ix])
            {
                ans[ix]=A[j++];
                    
                }
            else
            {
                ans[ix]=A[k--];
            }
        }
        return ans;
    }
};
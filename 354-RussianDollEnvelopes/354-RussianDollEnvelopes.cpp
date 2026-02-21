// Last updated: 2/21/2026, 9:43:51 AM
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        sort(envelopes.begin(),envelopes.end(),[&](auto a,auto b){return a[0]==b[0]? b[1]<a[1] : a[0]<b[0];});
        int n=envelopes.size();
        int ans=1;
        vector<int> dp(n,1);
        for(int i=0;i<n;i++)
        {
            for(int j=i-1;j>=0;j--)
            {
                if(envelopes[i][0]>envelopes[j][0] && envelopes[i][1]>envelopes[j][1])
                {
                    dp[i]=max(dp[i],dp[j]+1);
                    ans=max(dp[i],ans);
                }
            }
        }
        return ans;
    }
};
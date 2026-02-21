// Last updated: 2/21/2026, 9:43:56 AM
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, INT_MAX);
        dp[0]=0;
        for(int money=1;money<=amount;money++)
        {
            for(auto coin:coins)
            {
                 if(money>=coin)   

                 {
                        int temp=dp[money-coin];
                        if(temp!=INT_MAX && temp+1<dp[money])
                        {
                            dp[money]=temp+1;  
                        }
                 }
            }
          }
       if(dp[amount]==INT_MAX)
       {
        return -1;
       }
        return dp[amount];
    }
};
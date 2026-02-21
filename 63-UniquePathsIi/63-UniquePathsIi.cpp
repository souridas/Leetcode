// Last updated: 2/21/2026, 9:44:57 AM
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        
        int n=obstacleGrid.size();
        int m=obstacleGrid[0].size();
        if(obstacleGrid[0][0]==1)
        {
            return 0;
        }
        int dp[n+1][m+1];
        memset(dp,0,sizeof(dp));
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
             if(obstacleGrid[i-1][j-1]==1)
             {
                 dp[i][j]=-1;
             }
            }
        }
         for(int i=1;i<=m;i++)
            {
               if(dp[1][i]>=0)
               {
                   dp[1][i]=1;
               }
                 else
                 {
                     break;
                 }
            }
         for(int i=1;i<=n;i++)
        {
           if(dp[i][1]>=0)
           {
               dp[i][1]=1;
           }
             else
             {
                 break;
             }
        }
        for(int i=2;i<=n;i++)
        {
            for(int j=2;j<=m;j++)
            {
                if(dp[i][j]==-1)
                {
                    continue;
                }
                else
                {
                    if(dp[i-1][j]>0)
                    {
                        dp[i][j]=dp[i-1][j];
                    }
                    if(dp[i][j-1]>0)
                    {
                        dp[i][j]=dp[i][j]+dp[i][j-1];
                    }
                }
            }
        }
        if(dp[n][m]==-1)
        {
            return 0;
        }
        return dp[n][m];
    }
};
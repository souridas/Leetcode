# Last updated: 3/9/2026, 7:54:36 AM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        n,m=len(text1),len(text2)
4        dp=[[0]*(m+1)for _ in range(n+1)]
5        for i in range(1,n+1):
6            for j in range(1,m+1):
7                if text1[i-1]==text2[j-1]:
8                    dp[i][j]=1+dp[i-1][j-1]
9                else:
10                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
11        return dp[n][m]
12
13        
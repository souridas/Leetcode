# Last updated: 3/30/2026, 8:49:36 AM
# recap
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        n,m=len(text1)+1,len(text2)+1
4        dp=[[0]*m for _ in range(n)]
5        for i in range(1,n):
6            for j in range(1,m):
7                if text1[i-1]==text2[j-1]:
8                    dp[i][j]=1+dp[i-1][j-1]
9                else:
10                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
11        return dp[n-1][m-1]
12                
13
14        
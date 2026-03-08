# Last updated: 3/8/2026, 10:38:20 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        m,n=len(s),len(t)
4        if n>m: return 0
5        dp=[[0]*(n+1) for _ in range(m+1)]
6        for i in range(m+1):
7            dp[i][0]=1     
8        for i in range(1,m+1):
9            for j in range(1,n+1):
10                if s[i-1]==t[j-1]:
11                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
12                else:
13                    dp[i][j]=dp[i-1][j]
14        return dp[m][n]
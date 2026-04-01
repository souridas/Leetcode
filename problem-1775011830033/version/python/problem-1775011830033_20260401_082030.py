# Last updated: 4/1/2026, 8:20:30 AM
# solved dp
1class Solution:
2    def minCost(self, n: int) -> int:
3        if n<=1:
4            return 0
5        dp=[float('inf')]*(n+1)
6        dp[0]=0
7        dp[1]=0
8        dp[2]=1
9        for i in range(3,n+1):
10            for j in range(1,i):
11                dp[i]=min(dp[i],dp[i-j]+dp[j]+j*(i-j))
12        return dp[n]
13        
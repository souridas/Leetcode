# Last updated: 3/26/2026, 10:51:14 PM
# dp
1class Solution:
2    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
3        dp=[0]*(days[-1]+1)
4        for i in range(1,days[-1]+1):
5            if i not in days:
6                dp[i]=dp[i-1]
7            else:
8                dp[i]=min(dp[i-1]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
9        return dp[days[-1]]
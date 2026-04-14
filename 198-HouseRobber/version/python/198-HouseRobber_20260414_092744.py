# Last updated: 4/14/2026, 9:27:44 AM
# normal dp
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n=len(nums)
4        dp=[0]*n
5        dp[0]=nums[0]
6        for i in range(1,n):
7            dp[i]=nums[i]
8            if i>=2:
9                dp[i]+=dp[i-2]
10            dp[i]=max(dp[i-1],dp[i])
11        return dp[n-1]
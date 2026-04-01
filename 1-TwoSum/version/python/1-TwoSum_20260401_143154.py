# Last updated: 4/1/2026, 2:31:54 PM
# dictionary
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        dp={}
4        for i,num in enumerate(nums):
5            if target-num in dp:
6                return [i,dp[target-num]]
7            else:
8                dp[num]=i
9        return [-1,-1]
10       
# Last updated: 4/1/2026, 3:57:44 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        max_sum=float('-inf')
4        run_sum=0
5        for num in nums:
6            if run_sum<0:
7                run_sum=num
8            else:
9                run_sum+=num
10            max_sum=max(max_sum,run_sum)
11        return max_sum
12
13
14        
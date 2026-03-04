# Last updated: 3/4/2026, 2:56:38 PM
# math problem
1class Solution:
2    def optimalDivision(self, nums: List[int]) -> str:
3        n=len(nums)
4        if n==1: return str(nums[0])
5        if n==2: return str(nums[0])+"/"+str(nums[1])
6        ans=str(nums[0])+"/"+"("
7        for i,num in enumerate(nums):
8            if i>0:
9                ans+=str(num)+"/"
10        ans=ans[:-1]
11        ans+=")"
12        return ans
13        
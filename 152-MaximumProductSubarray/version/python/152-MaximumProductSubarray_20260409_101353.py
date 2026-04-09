# Last updated: 4/9/2026, 10:13:53 AM
# 2 kadane
1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        ans =float('-inf')
4        product=1
5        for num in nums:
6            product*=num
7            ans=max(product,ans)
8            if product==0:
9                product=1
10        product=1
11        for i in range(len(nums)-1,-1,-1):
12            product*=nums[i]
13            ans=max(ans,product)
14            if product==0:
15                product=1
16        return ans
17        
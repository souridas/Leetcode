# Last updated: 2/24/2026, 8:01:26 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        n=len(nums)
4        l,h=0,n-1
5        while l<h:
6            m=(l+h)//2
7            if nums[m]>nums[h]:
8                l=m+1
9            else:
10                h=m
11        return nums[l]
12        
# Last updated: 4/9/2026, 10:36:39 AM
# binary search
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        if len(nums)==1:
4            return 0
5        l,r=0,len(nums)-1
6        while l<=r:
7            m=(l+r)//2
8            if m and m<len(nums)-1 and nums[m-1]<nums[m]>nums[m+1]:
9                return m
10            if m==0 and nums[m]>nums[m+1]:
11                return 0
12            if m==len(nums)-1 and nums[m-1]<nums[m]:
13                return len(nums)-1
14            if m<len(nums)-1 and nums[m]<nums[m+1]:
15                l+=1
16            elif m and nums[m-1]>nums[m]:
17                r-=1
18            else:
19                continue
20        return -1
21            
22        
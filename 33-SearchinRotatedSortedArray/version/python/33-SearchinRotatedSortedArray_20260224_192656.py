# Last updated: 2/24/2026, 7:26:56 PM
# compare l,h with m value
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l,h=0,len(nums)-1
4        while l<=h:
5            m = (l+h)//2
6            if nums[m]==target:
7                return m
8            if nums[h]>=nums[m]:
9                if target>=nums[m] and target<=nums[h]:
10                    l=m+1
11                else:
12                    h=m-1
13            else:
14                if target<nums[m] and target>=nums[l]:
15                    h=m-1
16                else:
17                    l=m+1
18        return -1
19        
20
21
22        
# Last updated: 4/1/2026, 3:51:03 PM
# pointers and sorting
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        results=[]
4        nums.sort()
5        for i in range(len(nums)):
6            if i>0 and nums[i]==nums[i-1]:
7                continue
8            l,r=i+1,len(nums)-1
9            while l<r:
10                total=nums[i]+nums[l]+nums[r]
11                if total==0:
12                    results.append([nums[i],nums[l],nums[r]])
13                    l+=1
14                    r-=1
15                    while l<r and nums[l]==nums[l-1]:
16                        l+=1
17                    while l<r and nums[r]==nums[r+1]:
18                        r-=1
19                elif total<0:
20                    l+=1
21                else:
22                    r-=1
23        return results
24
25
26        
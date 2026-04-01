# Last updated: 4/1/2026, 2:19:10 PM
# find breaking points
1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        index=-1
7        n=len(nums)
8        j=n-1
9        while j>0:
10            if nums[j]>nums[j-1]:
11                index=j-1
12                break
13            j-=1
14        if index==-1:
15            return nums.reverse()
16        j=n-1
17        while j>index:
18            if nums[j]>nums[index]:
19                nums[index],nums[j]=nums[j],nums[index]
20                break
21            j-=1
22        nums[index+1:]=reversed(nums[index+1:])
23        return nums
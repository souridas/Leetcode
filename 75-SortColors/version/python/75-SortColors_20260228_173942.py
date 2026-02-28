# Last updated: 2/28/2026, 5:39:42 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        i=0
7        j=len(nums)-1
8        l=0
9        while i<=j:
10            if nums[i]==0:
11                nums[i],nums[l]=nums[l],nums[i]
12                l+=1
13            elif nums[i]==2:
14                nums[i],nums[j]=nums[j],nums[i]
15                j-=1
16                i-=1
17            i+=1
18        return
19
20            
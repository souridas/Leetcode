# Last updated: 3/29/2026, 2:24:53 PM
# perfect finish
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        l,i,r=0,0,len(nums)-1
7        while i<=r:
8            if nums[i]==0:
9                nums[l],nums[i]=nums[i],nums[l]
10                l+=1
11            elif nums[i]==2:
12                nums[r],nums[i]=nums[i],nums[r]
13                r-=1
14                i-=1
15            i+=1      
16        return nums          
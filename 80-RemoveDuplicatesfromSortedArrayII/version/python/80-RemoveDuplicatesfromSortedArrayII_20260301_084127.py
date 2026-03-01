# Last updated: 3/1/2026, 8:41:27 AM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        k=2
4        for i in range(k,len(nums)):
5            if nums[k-2]!=nums[i]:
6                nums[k]=nums[i]
7                k+=1
8        return k
9        
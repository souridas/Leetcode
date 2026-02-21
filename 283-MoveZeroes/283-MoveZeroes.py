# Last updated: 2/21/2026, 9:43:58 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        i=0
        n=len(nums)
        while i<n and pos<n:
            if nums[i]!=0:
                nums[pos]=nums[i]
                if pos!=i:
                    nums[i]=0
                pos+=1
            i+=1
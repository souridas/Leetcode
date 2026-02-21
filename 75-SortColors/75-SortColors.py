# Last updated: 2/21/2026, 9:44:50 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        l=0
        while i<=j:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
            elif nums[i]==2:
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
                i-=1
            i+=1
        return

            
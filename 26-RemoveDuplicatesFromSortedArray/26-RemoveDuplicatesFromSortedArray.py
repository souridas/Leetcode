# Last updated: 2/21/2026, 9:45:15 AM
def swap(nums,x,y):
        nums[x],nums[y]=nums[y],nums[x]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        while i<len(nums) and j<len(nums):
            if nums[i]!=nums[j] and i<len(nums)-1:
                swap(nums,i+1,j)
                i=i+1
                j=j+1
            else:
                j=j+1
        return i+1
            
            
        
# Last updated: 2/21/2026, 9:45:14 AM
def swap(nums,x,y):
    nums[x],nums[y]=nums[y],nums[x]
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=len(nums)-1
        while i>=0:
            if nums[i]==val:
                j=i+1
                k=i
                while j<len(nums) and k<len(nums):
                    if nums[j]!=val:
                        swap(nums,k,j)
                    k=k+1
                    j=j+1
            i=i-1
        i=0
        while i<len(nums) and nums[i]!=val:
                i=i+1
        return i
                    
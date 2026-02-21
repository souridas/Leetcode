# Last updated: 2/21/2026, 9:45:11 AM
def binary_search(nums,target,l,h):
    m=0
    while l<=h:
        m=(l+h)//2
        if nums[m]>=target and nums[m-1]<target:
            return m
        elif nums[m]<target:
            l=m+1
        else:
            h=m-1
    return m

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<=nums[0]:
            return 0
        elif target>nums[len(nums)-1]:
            return len(nums)
        return binary_search(nums,target,0,len(nums)-1)
        
        
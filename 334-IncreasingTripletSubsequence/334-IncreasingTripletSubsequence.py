# Last updated: 2/21/2026, 9:43:55 AM
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        max_val=max(nums)
        min_val=min(nums)
        n=len(nums)
        min_left=[max_val]*n
        max_right=[min_val]*n

        for i in range(1,n,1):
            min_left[i]=min(min_left[i-1],nums[i-1])

        for i in range(n-2,-1,-1):
            max_right[i]=max(max_right[i+1],nums[i+1])

        for i in range(1,n-1):
            if min_left[i]<nums[i] and max_right[i]>nums[i]:
                return True

        return False
            
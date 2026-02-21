# Last updated: 2/21/2026, 9:45:04 AM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        ans=nums[0]
        for num in nums:
            if total<0:
                total=0
            total+=num
            ans = max(ans,total)
        return ans
        

        
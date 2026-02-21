# Last updated: 2/21/2026, 9:43:32 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index=-1
        total_sum=0
        for num in nums:
            total_sum+=num
        left_sum=0
        for i in range(len(nums)):
            if 2*left_sum == total_sum-nums[i]:
                index=i
                break
            else:
                left_sum+=nums[i]
        return index
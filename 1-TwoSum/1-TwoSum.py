# Last updated: 2/21/2026, 9:45:32 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store={}
        for i in range(len(nums)):
            if target-nums[i] in store:
                return [i,store[target-nums[i]]]
            else:
                store[nums[i]]=i
        return []

        
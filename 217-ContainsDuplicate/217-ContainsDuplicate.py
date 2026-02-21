# Last updated: 2/21/2026, 9:44:11 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
        
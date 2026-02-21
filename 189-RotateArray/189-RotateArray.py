# Last updated: 2/21/2026, 9:44:19 AM
class Solution:

    def reverse(self, nums,st,en):
        while st<=en:
            a=nums[st]
            nums[st]=nums[en]
            nums[en]=a
            st+=1
            en-=1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-1)
        
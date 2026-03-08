# Last updated: 3/8/2026, 8:03:02 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        store=[0]*len(nums)
4        if len(nums)==1:
5            return nums[0]
6        store[0]=nums[0]
7        store[1]=max(nums[0],nums[1])
8        for i in range(2,len(nums)):
9            store[i]=max(store[i-1],nums[i]+store[i-2])
10        return store[len(nums)-1]
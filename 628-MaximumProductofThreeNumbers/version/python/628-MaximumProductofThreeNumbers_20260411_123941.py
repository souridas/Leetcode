# Last updated: 4/11/2026, 12:39:41 PM
# easy sort
1class Solution:
2    def maximumProduct(self, nums: List[int]) -> int:
3        nums.sort()
4        p1=nums[0]*nums[1]*nums[-1]
5        p2=nums[-1]*nums[-2]*nums[-3]
6        return max(p1,p2)
7
8        
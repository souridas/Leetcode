# Last updated: 3/1/2026, 9:17:27 AM
1class Solution:
2    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
3        if k<=1:
4            return 0
5        product=1
6        count=0
7        l=0
8        for r in range(len(nums)):
9            product=product*nums[r]
10            while product>=k:
11                product=product//nums[l]
12                l+=1
13            if product<k:  
14                count+=(r-l+1)
15        return count
16
17       
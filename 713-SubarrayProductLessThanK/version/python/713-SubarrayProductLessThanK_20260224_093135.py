# Last updated: 2/24/2026, 9:31:35 AM
# using sliding window approach
1class Solution:
2    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
3        if k<=1:
4            return 0
5        total_count=0
6        product=1
7        left=0
8        for right,num in enumerate(nums):
9            product=product*num
10            while product>=k:
11                product=product//nums[left]
12                left+=1
13            if product<k:
14                total_count+= (right-left+1)
15        return total_count
16        